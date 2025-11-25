import json
import argparse
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "tasks.json"


def load_tasks():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)
    print(f"Tasks saved to: {DATA_FILE.resolve()}")


def add_task(title, due=None, priority="normal"):
    tasks = load_tasks()

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "due": due,
        "priority": priority,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {title}")


def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['title']} - Priority: {task['priority']}")


def search_tasks(keyword):
    tasks = load_tasks()
    results = [t for t in tasks if keyword.lower() in t["title"].lower()]

    if not results:
        print("No matching tasks found.")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ADD COMMAND
    add_cmd = subparsers.add_parser("add", help="Add a new task")
    add_cmd.add_argument("title", help="Task title")
    add_cmd.add_argument("--due", help="Due date (YYYY-MM-DD)")
    add_cmd.add_argument("--priority", choices=["low", "normal", "high"], default="normal")

    # LIST COMMAND
    subparsers.add_parser("list", help="List all tasks")

    # SEARCH COMMAND
    search_cmd = subparsers.add_parser("search", help="Search tasks")
    search_cmd.add_argument("keyword", help="Keyword to search for")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.due, args.priority)
    elif args.command == "list":
        list_tasks()
    elif args.command == "search":
        search_tasks(args.keyword)


# ✅ This line actually runs your program
if __name__ == "__main__":
    main()