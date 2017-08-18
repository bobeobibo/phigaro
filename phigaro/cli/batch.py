import argparse
import logging
import multiprocessing
import os
import sys
import uuid
from os.path import join

import yaml

from phigaro.context import Context
from phigaro.scheduling.path import sample_name
from phigaro.scheduling.runner import run_tasks_chain
from phigaro.scheduling.task.gene_mark import GeneMarkTask
from phigaro.scheduling.task.hmmer import HmmerTask
from phigaro.scheduling.task.run_phigaro import RunPhigaroTask


def main():
    default_config_path = join(os.getenv('HOME'), '.phigaro.yml')
    parser = argparse.ArgumentParser(
        description='Phigaro is a scalable command-line tool for predictions phages and prophages '
                    'from nucleid acid sequences (including metagenomes) and '
                    'is based on phage genes HMMs and a smoothing window algorithm.', )
    parser.add_argument('-f', '--fasta-file', help='Assembly scaffolds\contigs or full genomes', required=True)
    parser.add_argument('-c', '--config', default=default_config_path, help='config file')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-t', '--threads',
                        type=int,
                        default=multiprocessing.cpu_count(),
                        help='num of threads ('
                             'default is num of CPUs={})'.format(multiprocessing.cpu_count()))

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARN)
    logging.getLogger('sh.command').setLevel(logging.WARN)

    with open(args.config) as f:
        config = yaml.load(f)

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

    gene_mark_task = GeneMarkTask(filename)
    hmmer_task = HmmerTask(gene_mark_task=gene_mark_task)
    run_phigaro_task = RunPhigaroTask(gene_mark_task=gene_mark_task, hmmer_task=hmmer_task)

    output_file = run_tasks_chain([
        gene_mark_task,
        hmmer_task,
        run_phigaro_task
    ])

    with open(output_file) as f:
        for line in f:
            sys.stdout.write(line)


if __name__ == '__main__':
    main()
