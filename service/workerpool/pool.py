import os
import queue
import weakref

from . import task
from . import worker


class WorkerPool:
    """
    Класс контролирующий поведение воркеров
    """

    def __init__(self):
        self.queue = queue.PriorityQueue()
        self.workers = [worker.Worker(self.queue, number) for number in range(os.cpu_count())]
        self.tasks_refs = weakref.WeakValueDictionary()

    def put_task(self, task):
        """
        Помещение задачи в очередь выполнения
        :param task: объект класса Task описывающий задчу
        :param task_status: статус задачи
        :return: None
        """
        self.tasks_refs[task.id] = task
        self.queue.put(task)

    def delete_task(self, task_id):
        """
        Отмена конкретной задачи
        :param task_id: идентификатор задачи
        :return: None
        """
        try:
            self.tasks_refs[task_id]().delete()
        except AttributeError:
            pass

    def start(self):
        """
        Запуск пула воркеров
        :return: None
        """
        for current_worker in self.workers:
            current_worker.start()

    def stop(self):
        """
        Остановка пула воркеров
        :return: None
        """
        for current_worker in self.workers:
            self.queue.put(task.TaskStopper)
            current_worker.stop()
            current_worker.join()