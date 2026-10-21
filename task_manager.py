
__version__ = "1.0.0"


class TaskManager:
    """Класс для создания, поиска и управления задачами."""

    def __init__(self):
        """Создаёт пустой список задач."""
        self.tasks = []

    def add_task(self, title):
        """Добавляет задачу с указанным названием.

        Args:
            title: Название новой задачи.

        Raises:
            ValueError: Если название пустое.
        """
        if not title.strip():
            raise ValueError("Название задачи не может быть пустым")
        self.tasks.append({"title": title, "done": False})

    def complete_task(self, index):
        """Помечает задачу как выполненную.

        Args:
            index: Индекс задачи.

        Raises:
            IndexError: Если индекс некорректный.
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Некорректный индекс задачи")
        self.tasks[index]["done"] = True

    def delete_task(self, index):
        """Удаляет задачу по индексу.

        Args:
            index: Индекс удаляемой задачи.

        Raises:
            IndexError: Если индекс некорректный.
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Некорректный индекс задачи")
        self.tasks.pop(index)

    def get_tasks(self):
        """Возвращает список всех задач."""
        return self.tasks

    def search_tasks(self, query):
        """Ищет задачи по части названия без учёта регистра.

        Args:
            query: Поисковый запрос.

        Returns:
            Список найденных задач.
        """
        return [
            task for task in self.tasks
            if query.lower() in task["title"].lower()
        ]
