import peewee
import cherrypy


class OrmSqlitePlugin(cherrypy.process.plugins.SimplePlugin):
    """
    Плагин подключения к Sqlite-базе
    """

    def __init__(self, bus):
        super().__init__(bus)
        self.subscribe()
        self._database = None

    @property
    def database(self):
        return self._database

    def start(self):
        """
        Опдключение к sqlite
        :return: None
        """
        self._database = peewee.SqliteDatabase(cherrypy.config['sqlite']['path'])
        try:
            self._database.connect()
        except Exception:
            self.bus.log('Sqlite connection error!', traceback=True)
            self.bus.stop()
        self.bus.log('Sqlite connection successful')

    def stop(self):
        """
        Закрытие соединения
        :return: None
        """
        if not self._database.is_closed():
            self._database.close()
            self.bus.log('Sqlite connection closed')