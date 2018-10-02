from __future__ import absolute_import

import argparse
import logging
import multiprocessing
import os
import sys
import uuid
from os.path import join, exists

import yaml

from phigaro.context import Context
from phigaro.batch.runner import run_tasks_chain
from phigaro.batch.task.path import sample_name
from phigaro.batch.task.prodigal import ProdigalTask
from phigaro.batch.task.hmmer import HmmerTask
from phigaro.batch.task.dummy import DummyTask
from phigaro.batch.task.run_phigaro import RunPhigaroTask
from phigaro._version import __version__


def parse_substitute_output(subs):
    subs = subs or []
    res = {}
    for sub in subs:
        task_name, output = sub.split(":")
        res[task_name] = DummyTask(output, task_name)
    return res


def create_task(substitutions, task_class, *args, **kwargs):
    # TODO: refactor to class Application
    task = task_class(*args, **kwargs)
    if task.task_name in substitutions:
        print('Substituting output for {}: {}'.format(
            task.task_name, substitutions[task.task_name].output()
        ))

        return substitutions[task.task_name]
    return task


def main():
    default_config_path = join(os.getenv('HOME'), '.phigaro', 'config.yml')
    parser = argparse.ArgumentParser(
        prog='phigaro',
        description='Phigaro is a scalable command-line tool for predictions phages and prophages '
                    'from nucleid acid sequences',
    )

    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('-f', '--fasta-file', help='Assembly scaffolds/contigs or full genomes, required',
                        required=True)
    parser.add_argument('-c', '--config', default=default_config_path, help='Config file, not required')
    parser.add_argument('-v', '--verbose', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('-o', '--output', help='Output file, not required, default is stdout')
    parser.add_argument('-p', '--print-vogs', help='Print phage vogs for each region', action='store_true')
    parser.add_argument('-t', '--threads',
                        type=int,
                        default=multiprocessing.cpu_count(),
                        help='Num of threads ('
                             'default is num of CPUs={})'.format(multiprocessing.cpu_count()))

    parser.add_argument('--no-cleanup', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('-S', '--substitute-output', action='append', help=argparse.SUPPRESS)

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARN)
    logging.getLogger('sh.command').setLevel(logging.WARN)

    logger = logging.getLogger(__name__)

    if not exists(args.config):
        # TODO: pretty message
        print('Please create config file using phigaro-setup script')
        exit(1)

    with open(args.config) as f:
        logger.info('Using config file: {}'.format(args.config))
        config = yaml.load(f)

    config['phigaro']['print_vogs'] = args.print_vogs

    filename = args.fasta_file
    sample = '{}-{}'.format(
        sample_name(filename),
        uuid.uuid4().hex
    )

    Context.initialize(
        sample=sample,
        config=config,
        threads=args.threads,
    )

    substitutions = parse_substitute_output(args.substitute_output)

    prodigal_task = create_task(substitutions,
                                 ProdigalTask,
                                 filename)
    hmmer_task = create_task(substitutions,
                             HmmerTask,
                             prodigal_task=prodigal_task)

    run_phigaro_task = create_task(substitutions,
                                   RunPhigaroTask,
                                   prodigal_task=prodigal_task,
                                   hmmer_task=hmmer_task)

    tasks = [
        prodigal_task,
        hmmer_task,
        run_phigaro_task
    ]
    task_output_file = run_tasks_chain(tasks)

    with open(task_output_file) as f:
        out_f = open(args.output, 'w') if args.output else sys.stdout
        for line in f:
            out_f.write(line)
        if out_f is sys.stdout:
            out_f.close()

    if not args.no_cleanup:
        for t in tasks:
            t.clean()

if __name__ == '__main__':
    main()
