import cherrypy

import config
import plugins
import handlers


class ApplicationRoot:
    """
    Корневой обработчик сервиса
    """

    tasks = handlers.TaskHandler()

    def __init__(self):
        cherrypy.engine.orm = plugins.OrmSqlitePlugin(cherrypy.engine)
        cherrypy.engine.task_manager = plugins.TaskManagerPlugin(cherrypy.engine)


if __name__ == '__main__':
    cherrypy.quickstart(ApplicationRoot(), '/', config.CONFIG)