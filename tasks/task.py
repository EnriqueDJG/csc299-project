import time
import uuid

class Task:
    def __init__(self, title, description="", due_date=None, done=False, id=None, created_at=None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date  # Example format: "2024-12-01"
        self.done = done
        self.created_at = created_at or time.time()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "done": self.done,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description", ""),
            due_date=data.get("due_date"),
            done=data.get("done", False),
            created_at=data.get("created_at")
        )
