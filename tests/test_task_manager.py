
import pytest
from task_manager import TaskManager


@pytest.fixture
def manager():
    return TaskManager()


def test_add_task(manager):
    """Проверка добавления задачи."""
    manager.add_task("Изучить GitHub Actions")

    tasks = manager.get_tasks()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Изучить GitHub Actions"
    assert tasks[0]["done"] is False


def test_add_multiple_tasks(manager):
    """Проверка добавления нескольких задач."""
    manager.add_task("Первая задача")
    manager.add_task("Вторая задача")

    assert len(manager.get_tasks()) == 2


def test_complete_task(manager):
    """Проверка выполнения задачи."""
    manager.add_task("Написать тесты")
    manager.complete_task(0)

    assert manager.get_tasks()[0]["done"] is True


def test_delete_task(manager):
    """Проверка удаления задачи."""
    manager.add_task("Задача для удаления")
    manager.delete_task(0)

    assert len(manager.get_tasks()) == 0


def test_empty_task(manager):
    """Проверка запрета пустого названия."""
    with pytest.raises(ValueError):
        manager.add_task("")


def test_whitespace_task(manager):
    """Проверка названия из пробелов."""
    with pytest.raises(ValueError):
        manager.add_task("   ")

# Sipmply a new line
def test_initial_tasks_empty(manager):
    """Проверка пустого списка при создании."""
    assert manager.get_tasks() == []


def test_complete_one_of_multiple_tasks(manager):
    """Проверка выполнения только выбранной задачи."""
    manager.add_task("Первая задача")
    manager.add_task("Вторая задача")

    manager.complete_task(0)

    assert manager.get_tasks()[0]["done"] is True
    assert manager.get_tasks()[1]["done"] is False


def test_search_tasks(manager):
    """Поиск задачи по части названия."""
    manager.add_task("Изучить GitHub Actions")
    manager.add_task("Написать тесты")
    manager.add_task("Изучить Python")

    results = manager.search_tasks("Изучить")

    assert len(results) == 2


def test_search_case_insensitive(manager):
    """Поиск без учёта регистра."""
    manager.add_task("Изучить Python")

    results = manager.search_tasks("python")

    assert len(results) == 1
    assert results[0]["title"] == "Изучить Python"


def test_search_no_results(manager):
    """Поиск отсутствующей задачи."""
    manager.add_task("Написать тесты")

    results = manager.search_tasks("Java")

    assert results == []
