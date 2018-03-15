import queue
import threading

import cherrypy


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
            try:
                current_task = self.queue.get_nowait()
            except queue.Empty:
                continue
            if current_task.deleted:
                continue
        cherrypy.log('WORKER #{} stopped'.format(self.id))