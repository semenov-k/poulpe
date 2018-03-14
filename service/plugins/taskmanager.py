import cherrypy

import workerpool


class TaskManagerPlugin(cherrypy.process.plugins.SimplePlugin):
    """
    Плагин инициализации воркеров и запуска очереди задач
    """

    def __init__(self, bus):
        super().__init__(bus)
        self._pool = workerpool.WorkerPool()
        self.subscribe()

    @property
    def pool(self):
        return self._pool

    def start(self):
        """
        Запуск пула воркеров
        :return: None
        """
        self._pool.start()
        self.bus.log('Workers started')

    def stop(self):
        """
        Корректное завершение пула воркеров
        :return: None
        """
        self._pool.stop()
        self.bus.log('Workers stopped')