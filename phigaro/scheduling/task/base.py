import abc
from shutil import rmtree

import six

from phigaro.context import Context
from phigaro.scheduling.path import directory, file, path


@six.add_metaclass(abc.ABCMeta)
class AbstractTask(object):
    task_name = None

    def __init__(self):
        if self.task_name is None:
            raise Exception("{}.task_name must by set".format(self.__class__.__name__))

        self.directory()
        self.context = Context.instance()
        self.sample = self.context.sample
        self.config = self.context.config
        self._prepare()

    def _prepare(self):
        pass

    @abc.abstractmethod
    def output(self):
        """
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def run(self):
        pass

    def directory(self, *items):
        return directory(self.task_name, *items)

    def file(self, *items):
        return file(self.task_name, *items)

    def clean(self):
        rmtree(path(self.task_name))





