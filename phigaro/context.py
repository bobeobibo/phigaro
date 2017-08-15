from singleton.singleton import Singleton


@Singleton
class Context(object):
    def __init__(self, sample, threads, config):
        """

        :type sample: str
        :type config: dict
        :type threads: int
        """
        self.threads = threads
        self.sample = sample
        self.config = config
