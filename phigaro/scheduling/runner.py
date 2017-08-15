from .task.base import AbstractTask

import logging
logger = logging.getLogger(__name__)


def make_tasks_chain(task_classes, sample, first_input, context):
    """
    :type task_classes: list[(str, str, Context)->AbstractTask]
    :type first_input: str
    :type sample: str
    :type context: Context
    :rtype: list[AbstractTask]
    """

    input = first_input
    tasks = []
    for task_class in task_classes:
        task = task_class(input, sample, context)
        input = task.output()
        tasks.append(task)

    return tasks


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
