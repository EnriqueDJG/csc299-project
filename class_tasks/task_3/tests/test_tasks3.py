from tasks3.manager import add_task, load_tasks, complete_task

def test_add_task():
    add_task("Pytest Task")
    tasks = load_tasks()
    assert any(t["title"] == "Pytest Task" for t in tasks)


def test_complete_task():
    add_task("Complete This")
    tasks = load_tasks()
    task_id = tasks[-1]["id"]
    complete_task(task_id)
    tasks = load_tasks()
    task = next(t for t in tasks if t["id"] == task_id)
    assert task["completed"] is True