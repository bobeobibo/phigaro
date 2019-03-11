from builtins import super

from .base import AbstractTask
import sh


class ProdigalTask(AbstractTask):
    task_name = 'prodigal'

    def __init__(self, preprocess_task):
        super().__init__()

        self.preprocess_task = preprocess_task
        self.prodigal = (
            sh.Command(self.config['prodigal']['bin'])
            .bake(
                i=self.preprocess_task.output(),
                a=self.output()
            )
        )

    def output(self):
        return self.file('{}.faa'.format(self.sample))

    def run(self):
        self.prodigal()