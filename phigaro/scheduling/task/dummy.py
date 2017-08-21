from builtins import super

from .base import AbstractTask


class DummyTask(AbstractTask):
    task_name = 'dummy'

    def __init__(self, output):
        super().__init__()
        self._output = output

    def run(self):
        pass

    def output(self):
        return self._output
