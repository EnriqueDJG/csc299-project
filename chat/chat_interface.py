# chat/chat_interface.py

class ChatInterface:
    def __init__(self, storage, note_manager, task_manager):
        self.storage = storage
        self.note_manager = note_manager
        self.task_manager = task_manager

    def start(self):
        print("=== Personal Knowledge & Task Management System ===")
        print("Type 'help' to see commands.")
        while True:
            cmd = input(">> ").strip()
            if cmd == "exit":
                break
            self.handle_command(cmd)

    def handle_command(self, cmd):
        if cmd == "help":
            self.show_help()
        elif cmd == "note create":
            self.create_note()
        elif cmd.startswith("note search"):
            _, _, keyword = cmd.partition(" ")
            self.search_notes(keyword)
        elif cmd.startswith("note delete"):
            _, _, note_id = cmd.partition(" ")
            self.delete_note(note_id)
        elif cmd == "task add":
            self.add_task()
        elif cmd.startswith("task done"):
            _, _, task_id = cmd.partition(" ")
            self.mark_task_done(task_id)
        elif cmd.startswith("task delete"):
            _, _, task_id = cmd.partition(" ")
            self.delete_task(task_id)
        elif cmd == "task list":
            self.list_tasks()
        else:
            print("Unknown command. Type 'help'.")

    def show_help(self):
        print("""
Commands:
  note create
  note search <keyword>
  note delete <id>
  task add
  task done <id>
  task delete <id>
  task list
  exit
""")

    # ---------- Notes ----------
    def create_note(self):
        title = input("Title: ")
        content = input("Content: ")
        tags = input("Tags (comma separated): ").split(",")
        self.note_manager.create_note(title, content, [t.strip() for t in tags])

    def search_notes(self, keyword):
        results = self.note_manager.search_notes(keyword)
        for row in results:
            print(row)

    def delete_note(self, note_id):
        self.note_manager.delete_note(note_id)

    # ---------- Tasks ----------
    def add_task(self):
        title = input("Title: ")
        description = input("Description: ")
        due = input("Due date (YYYY-MM-DD): ")
        self.task_manager.add_task(title, description, due)

    def list_tasks(self):
        tasks = self.task_manager.list_tasks()
        for row in tasks:
            print(row)

    def mark_task_done(self, task_id):
        self.task_manager.mark_done(task_id)

    def delete_task(self, task_id):
        self.task_manager.delete_task(task_id)
