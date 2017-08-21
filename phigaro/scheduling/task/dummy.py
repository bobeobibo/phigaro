from builtins import super

from .base import AbstractTask


class DummyTask(AbstractTask):
    task_name = 'dummy'

    def __init__(self, output, old_task_name):
        super().__init__()
        self._output = output
        self.task_name = '{}-dummy'.format(old_task_name)

    def run(self):
        pass

    def output(self):
        return self._output

    def clean(self):
        pass
