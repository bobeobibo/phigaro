from builtins import super

from .base import AbstractTask
import sh


class ProdigalTask(AbstractTask):
    task_name = 'prodigal'

    def __init__(self, input):
        super().__init__()

        self.input = input
        self.prodigal = (
            sh.Command(self.config['prodigal']['bin'])
            .bake(
                i=self.input,
                a=self.output()
            )
        )

    def output(self):
        return self.file('{}.faa'.format(self.sample))

    def run(self):
        self.prodigal()