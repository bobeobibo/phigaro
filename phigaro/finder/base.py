import abc
import six


class Phage(object):
    def __init__(self, begin, end, is_prophage):
        """

        :type begin: int
        :type end: int
        :type is_prophage: bool
        """
        self.begin = begin
        self.end = end
        self.is_prophage = is_prophage


@six.add_metaclass(abc.ABCMeta)
class AbstractFinder(object):
    @abc.abstractmethod
    def find_phages(self, bacteria_npn):
        """

        :type bacteria_npn: list[int]
        :rtype: list[Phage]
        """
        pass





