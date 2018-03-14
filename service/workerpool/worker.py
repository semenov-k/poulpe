import threading

import cherrypy

from . import task


class Worker(threading.Thread):
    """
    Класс воркера для запуска и обработки процессов
    """

    def __init__(self, queue, id):
        """
        Инициализация воркера
        :param queue: очередь задач
        :param id: идентификатор воркера
        """
        self.queue = queue
        self.id = id
        self.running = True

        super().__init__()

    def stop(self):
        """
        Установка флага о завершении треда воркера
        :return: None
        """
        self.running = False

    def run(self):
        cherrypy.log('WORKER #{} started'.format(self.id))
        while self.running:
            current_task = self.queue.get()
            if current_task is task.TaskStopper:
                break
        cherrypy.log('WORKER #{} stopped'.format(self.id))