import enum
import uuid
import functools


class StatusPriority(enum.Enum):
    """
    Приоритет задачи в зависимости от статуса с которым она запускается
    """
    STOPPER = 1
    LAUNCHED = 25
    SCHEDULED = 50
    NEW = 100


@functools.total_ordering
class OrderedItem:
    """
    Класс для сортировки внутри OrderedQueue
    """
    def __init__(self, status):
        self._priority = status.value

    def __eq__(self, other):
        return self._priority == other.priority

    def __lt__(self, other):
        return self._priority < other.priority


class TaskStopper(OrderedItem):
    """
    Класс завершающий прием задач из очереди
    """
    pass


class Task(OrderedItem):
    """
    Класс описывающий задачу
    """
    def __init__(self, alias, run_params, status=StatusPriority.NEW):
        super().__init__(status)
        self._id = uuid.uuid4().hex
        self._deleted = False
        self._alias = alias
        self._run_params = run_params

    @property
    def id(self):
        return self._id

    @property
    def priority(self):
        return self._priority

    @property
    def deleted(self):
        return self._deleted

    @property
    def run_params(self):
        return self._process_kwargs

    @property
    def alias(self):
        return self._alias

    def delete(self):
        """
        Отмена задачи
        :return: None
        """
        self._deleted = True
