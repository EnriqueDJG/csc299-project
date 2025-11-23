from ai.ai_agent import AIAgent

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
        
        elif cmd == "note list":
            self.list_notes()
        
        elif cmd == "task add":
            self.add_task()
        
        elif cmd.startswith("task done"):
            task_id = cmd.split("task done", 1)[1].strip()
            task_id = task_id.replace('"', '').replace("'", "")
            self.mark_task_done(task_id)
        
        elif cmd.startswith("task delete"):
            _, _, task_id = cmd.partition(" ")
            self.delete_task(task_id)
        
        elif cmd == "task list":
            self.list_tasks()
        
        elif cmd.startswith("ai summarize"):
            note_id = cmd.split("ai summarize", 1)[1].strip()
            self.ai_summarize(note_id)

        elif cmd.startswith("ai suggest"):
            note_id = cmd.split("ai suggest", 1)[1].strip()
            self.ai_suggest_tasks(note_id)
        
        else:
            print("Unknown command. Type 'help'.")

    def show_help(self):
        print("""
    Commands:

    NOTES
    note create              - Create a new note
    note list                - List all notes and their IDs
    note search <keyword>    - Search notes
    note delete <id>         - Delete a note

    TASKS
    task add                 - Add a new task
    task list                - List all tasks
    task done <id>           - Mark task as complete
    task delete <id>         - Delete a task

    AI
    ai summarize <note_id>   - Summarize a note using AI
    ai suggest <note_id>     - Generate tasks from a note

    SYSTEM
    help                     - Show this menu
    exit                     - Exit the program
    """)


    # ---------- Notes ----------
    def create_note(self):
        title = input("Title: ")
        content = input("Content: ")
        tags = input("Tags (comma separated): ").split(",")
        self.note_manager.create_note(title, content, [t.strip() for t in tags])
    
    def list_notes(self):
        notes = self.note_manager.list_notes()

        if not notes:
            print("📭 No notes found")
            return

        print("\n📘 Your Notes:")
        for note in notes:
            print(f"""
    ID: {note['id']}
    Title: {note['title']}
    Tags: {', '.join(note.get('tags', []))}
    -------------------------
    """)

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
        success = self.task_manager.mark_done(task_id)
        if success:
            print("✅ Task marked as done!")
        else:
            print("❌ Task ID not found.")


    def delete_task(self, task_id):
        self.task_manager.delete_task(task_id)
    
    def ai_summarize(self, note_id):
        note = self.note_manager.get_note_by_id(note_id)

        if not note:
            print("❌ Note not found")
            return

        print("\n🤖 AI Summary:\n")
        print(AIAgent.summarize(note["content"]))


    def ai_suggest_tasks(self, note_id):
        note = self.note_manager.get_note_by_id(note_id)

        if not note:
            print("❌ Note not found")
            return

        print("\n🤖 AI Suggested Tasks:\n")
        print(AIAgent.suggest_tasks(note["content"]))
