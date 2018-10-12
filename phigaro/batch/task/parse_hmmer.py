import csv
import logging
import re
from builtins import super
from itertools import groupby

from .base import AbstractTask
from .prodigal import GeneMarkTask
from .hmmer import HmmerTask

logger = logging.getLogger(__name__)

INFINITY = float('inf')


class ParseHmmerTask(AbstractTask):
    task_name = 'parse_hmmer'

    def __init__(self, hmmer_task, gene_mark_task):
        """

        :type hmmer_task: HmmerTask
        :type gene_mark_task: GeneMarkTask
        """
        super().__init__()
        self.hmmer_task = hmmer_task
        self.genemark_task = gene_mark_task

    def output(self):
        return self.file('{}.npn'.format(self.sample))

    def run(self):
        self._parse_hmmer_output()

    @staticmethod
    def parse_line(line):
        tokens = re.split(r'\s+', line)
        scaffold = '>' + line.split('>')[1]
        name = tokens[0]
        evalue = float(tokens[4])
        return scaffold, name, evalue

    def _parse_hmmer_output(self):
        max_evalue = self.config['hmmer']['e_value_threshold']

        with open(self.hmmer_task.output()) as f:
            lines_it = (
                self.parse_line(line.strip())
                for line in f
                if not line.startswith('#') and line.strip()
            )

            hmm_res = {}
            for scaffold, gene_name, evalue in lines_it:
                if scaffold not in hmm_res:
                    hmm_res[scaffold] = {}
                # Take minimum of all evalues for current gene_name
                if gene_name in hmm_res[scaffold]:
                    hmm_res[scaffold][gene_name] = min(evalue, hmm_res[scaffold][gene_name])
                else:
                    hmm_res[scaffold][gene_name] = evalue

        with open(self.genemark_task.output()) as f:
            with open(self.output(), 'w') as of:
                writer = csv.writer(of, delimiter='\t')
                lines_it = (
                    line.strip().split('\t')
                    for line in f
                    if line.startswith('>')
                )

                for scaffold, group in groupby(lines_it, key=lambda t: t[1]):
                    if scaffold not in hmm_res:
                        continue
                    scaffold_res = hmm_res[scaffold]

                    is_phage_it = (
                        scaffold_res.get(gene_name[1:], INFINITY) <= max_evalue
                        for gene_name, _ in group
                    )

                    is_phage_it = (
                        'P' if is_phage else 'N'
                        for is_phage in is_phage_it
                    )
                    writer.writerow((scaffold, ''.join(is_phage_it)))

