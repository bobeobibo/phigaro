from singleton.singleton import Singleton


@Singleton
class Context(object):
    def __init__(self, sample, threads, config):
        """
        :type sample: str
        :type config: dict
        :type threads: int
        :type threads: dict
        """
        self.threads = threads
        self.sample = sample
        self.config = config
        self.scaffolds_info = {}
