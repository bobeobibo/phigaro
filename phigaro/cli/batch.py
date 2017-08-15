import sys
import uuid

import yaml
import argparse
import logging
import multiprocessing


from phigaro.context import Context
from phigaro.scheduling.path import sample_name
from phigaro.scheduling.task.gene_mark import GeneMarkTask
from phigaro.scheduling.task.hmmer import HmmerTask
from phigaro.scheduling.task.run_phigaro import RunPhigaroTask
from phigaro.scheduling.runner import make_tasks_chain, run_tasks_chain


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fasta-file', help='Scaffolds')
    parser.add_argument('-c', '--config', default='config.yml', help='config file')
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
        # context = Context().load(yaml.load(f))
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

