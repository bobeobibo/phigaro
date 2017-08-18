from builtins import super
import re
import sh
from itertools import groupby
import csv

from .base import AbstractTask
from .gene_mark import GeneMarkTask


class HmmerTask(AbstractTask):
    task_name = 'hmmer'

    def __init__(self, gene_mark_task):
        """

        :type gene_mark_task: GeneMarkTask
        """
        super().__init__()
        self.gene_mark = gene_mark_task

    def _prepare(self):
        self.hmmer = (
            sh.Command(self.config['hmmer']['bin'])
        )
        self._tmp_hmmer_out = self.file('{}.hmmer_out'.format(self.sample))

    def output(self):
        return self.file('{}.npn'.format(self.sample))

    def run(self):
        self.hmmer('--cpu', self.context.threads,
                   '--notextw',
                   '--tblout', self._tmp_hmmer_out,
                   self.config['hmmer']['pvog_path'],
                   self.gene_mark.output())
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

        with open(self._tmp_hmmer_out) as f:
            it = (
                self.parse_line(line.strip())
                for line in f
                if not line.startswith('#') and line.strip()
            )

            hmm_res = {}
            for scaffold, name, evalue in it:
                if scaffold not in hmm_res:
                    hmm_res[scaffold] = {}
                hmm_res[scaffold][name] = 1 if evalue < max_evalue else 0

        with open(self.gene_mark.output()) as f:
            with open(self.output(), 'w') as of:
                writer = csv.writer(of, delimiter='\t')
                it = (
                    line.strip().split('\t')
                    for line in f
                    if line.startswith('>')
                )
                # for i in it:
                #     print(i)

                for scaffold, group in groupby(it, key=lambda t: t[1]):
                    scaffold_res = hmm_res[scaffold]

                    is_phage_it = (
                        scaffold_res.get(name[1:], 0)
                        for name, _ in group
                    )

                    is_phage_it = (
                        'P' if is_phage else 'N'
                        for is_phage in is_phage_it
                    )
                    writer.writerow((scaffold, ''.join(is_phage_it)))

