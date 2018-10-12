from .task.base import AbstractTask

import logging
logger = logging.getLogger(__name__)


def run_tasks_chain(tasks_chain):
    """
    :type tasks_chain: list[AbstractTask]
    :rtype: str
    """

    for task in tasks_chain:
        logger.info("Executing {task}. output: {output}".format(
            task=task.task_name,
            output=task.output()
        ))
        task.run()

    return task.output()
