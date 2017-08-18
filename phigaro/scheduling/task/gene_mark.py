from builtins import super

from .base import AbstractTask
import sh


class GeneMarkTask(AbstractTask):
    task_name = 'gene_mark'

    def __init__(self, input):
        super().__init__()

        self.input = input
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
