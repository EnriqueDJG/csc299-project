import json
import argparse
from pathlib import Path
from datetime import datetime

# Store tasks2.json next to this script
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "tasks2.json"


def load_tasks():
    """Load tasks from tasks2.json."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # If file is empty or corrupted, start fresh
            return []


def save_tasks(tasks):
    """Save tasks to tasks2.json."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def add_task(title, due=None, priority="normal"):
    """Add a new task."""
    tasks = load_tasks()

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "due": due,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {title}")


def list_tasks():
    """List all tasks."""
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks")
    print("=" * 50)
    for task in tasks:
        status = "DONE" if task["completed"] else "PENDING"
        print(f"[{task['id']}] {task['title']}")
        print(f"    Status:   {status}")
        print(f"    Priority: {task['priority']}")
        print(f"    Due:      {task.get('due', 'None')}")
        print("-" * 50)


def search_tasks(keyword):
    """Search tasks by keyword in title."""
    tasks = load_tasks()
    results = [t for t in tasks if keyword.lower() in t["title"].lower()]

    if not results:
        print("No matching tasks found.")
        return

    print(f"\nSearch results for '{keyword}':")
    print("=" * 50)
    for task in results:
        status = "DONE" if task["completed"] else "PENDING"
        print(f"[{task['id']}] {task['title']} ({status})")


def complete_task(task_id: int):
    """Mark a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked complete.")
            return
    print("Task not found.")


def delete_task(task_id: int):
    """Delete a task by id."""
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print("Task not found.")
        return

    # Re-number IDs to keep them tidy
    for i, task in enumerate(new_tasks, start=1):
        task["id"] = i

    save_tasks(new_tasks)
    print(f"Task {task_id} deleted.")


def update_task(task_id: int, new_title: str):
    """Update the title of a task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print("Task not found.")


def main():
    parser = argparse.ArgumentParser(description="PKMS Task Manager - Version 2")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ADD
    add_cmd = subparsers.add_parser("add", help="Add a new task")
    add_cmd.add_argument("title", help="Task title")
    add_cmd.add_argument("--due", help="Due date (YYYY-MM-DD)")
    add_cmd.add_argument(
        "--priority",
        choices=["low", "normal", "high"],
        default="normal",
        help="Task priority",
    )

    # LIST
    subparsers.add_parser("list", help="List all tasks")

    # SEARCH
    search_cmd = subparsers.add_parser("search", help="Search tasks by keyword")
    search_cmd.add_argument("keyword")

    # COMPLETE
    complete_cmd = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_cmd.add_argument("task_id", type=int)

    # DELETE
    delete_cmd = subparsers.add_parser("delete", help="Delete a task")
    delete_cmd.add_argument("task_id", type=int)

    # UPDATE
    update_cmd = subparsers.add_parser("update", help="Update a task title")
    update_cmd.add_argument("task_id", type=int)
    update_cmd.add_argument("new_title", help="New title for the task")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.due, args.priority)
    elif args.command == "list":
        list_tasks()
    elif args.command == "search":
        search_tasks(args.keyword)
    elif args.command == "complete":
        complete_task(args.task_id)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "update":
        update_task(args.task_id, args.new_title)


if __name__ == "__main__":
    main()