
__version__ = "1.0.0"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if not title.strip():
            raise ValueError("Название задачи не может быть пустым")
        self.tasks.append({"title": title, "done": False})

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Некорректный индекс задачи")
        self.tasks[index]["done"] = True

    def delete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Некорректный индекс задачи")
        self.tasks.pop(index)

    def get_tasks(self):
        return self.tasks

    def search_tasks(self, query):
        """Поиск задач по части названия без учёта регистра."""
        return [
            task for task in self.tasks
            if query.lower() in task["title"].lower()
        ]
