
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if not title.strip():
            raise ValueError("Название задачи не может быть пустым")
        self.tasks.append({"title": title, "done": False})

    def complete_task(self, index):
        self.tasks[index]["done"] = True

    def delete_task(self, index):
        self.tasks.pop(index)

    def get_tasks(self):
        return self.tasks
