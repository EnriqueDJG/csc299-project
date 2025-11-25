from .manager import add_task, list_tasks, complete_task

def inc(n: int) -> int:
    """Increment a number by 1."""
    return n + 1


def double(n: int) -> int:
    """Double a number."""
    return n * 2


def main():
    print("Tasks3 PKMS running...")
    list_tasks()

if __name__ == "__main__":
    main()