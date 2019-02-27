from builtins import super

import os

from .base import AbstractTask
import sh


class GeneMarkTask(AbstractTask):
    task_name = 'gene_mark'

    def __init__(self, input):
        super().__init__()

        self.input = input
        self._lst_file = input + '.lst'
        self.gene_mark = (
            sh.Command(self.config['genemark']['bin'])
            .bake(
                m=self.config['genemark']['mod_path'],
                A=self.output(),
            )
        )

    def output(self):
        return self.file('{}.faa'.format(self.sample))

    def run(self):
        self.gene_mark(self.input)

    def clean(self):
        os.unlink(self._lst_file)
