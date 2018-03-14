import cherrypy


class TaskHandler:

    @cherrypy.expose
    def create(self, owner, task_type, callback_url=None):
        """
        Обработчик создания заданий
        :param owner: код владельца задания
        :param task_type: тип задания
        :callback_url: URL для обратного вызова, None если клиент сам запрашивает статус процесса
        :return: идентификатор задачи или traceback при ошибке
        """
        pass

    @cherrypy.expose
    def status(self, owner, task_id=None):
        """
        Обработчик статуса заданий
        :param owner: код владельца задания
        :param task_id: идентификатор задачи
        :return: статус задачи c external_id, если external_id == None, то возвращается лист задач переданого владельца
        """
        pass

    @cherrypy.expose
    def delete(self, owner, task_id):
        """
        Обработчик удаления задания
        :param owner: код владельца задания
        :param task_id: идентификатор задачи
        :return: OK или traceback при ошибке
        """
        pass