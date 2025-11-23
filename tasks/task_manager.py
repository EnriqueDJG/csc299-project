from storage.json_storage import JSONStorage

class TaskManager:
    def __init__(self, storage: JSONStorage):
        self.storage = storage
        self.storage_key = "tasks"

    def add_task(self, title, description="", due_date=None):
        tasks = self.storage.load(self.storage_key)

        task = {
            "id": self.storage.generate_id(),
            "title": title,
            "description": description,
            "due_date": due_date,
            "done": False
        }

        tasks.append(task)
        self.storage.save(self.storage_key, tasks)
        return task

    def list_tasks(self):
        return self.storage.load(self.storage_key)

    def mark_done(self, task_id):
        tasks = self.storage.load(self.storage_key)
        updated = False

        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                updated = True

        self.storage.save(self.storage_key, tasks)
        return updated

    def delete_task(self, task_id):
        tasks = self.storage.load(self.storage_key)
        tasks = [t for t in tasks if t["id"] != task_id]
        self.storage.save(self.storage_key, tasks)
