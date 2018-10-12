from builtins import super

import sh

from .base import AbstractTask
from .prodigal import ProdigalTask


class HmmerTask(AbstractTask):
    task_name = 'hmmer'

    def __init__(self, prodigal_task):
        """

        :type prodigal_task: ProdigalTask
        """
        super().__init__()
        self.prodigal = prodigal_task

    def _prepare(self):
        self.hmmer = (
            sh.Command(self.config['hmmer']['bin'])
        )

    def output(self):
        return self.file('{}.hmmer_out'.format(self.sample))

    def run(self):
        self.hmmer('--cpu', self.context.threads,
                   '--notextw',
                   '--tblout', self.output(),
                   self.config['hmmer']['pvog_path'],
                   self.prodigal.output())


