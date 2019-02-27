from builtins import super

import sh

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

    def output(self):
        return self.file('{}.npn'.format(self.sample))

    def run(self):
        self.hmmer('--cpu', self.context.threads,
                   '--notextw',
                   '--tblout', self.output(),
                   self.config['hmmer']['pvog_path'],
                   self.gene_mark.output())


