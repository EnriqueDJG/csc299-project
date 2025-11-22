import time
import uuid

class Note:
    def __init__(self, title, content, tags=None, id=None, created_at=None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.content = content
        self.tags = tags or []
        self.created_at = created_at or time.time()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Note(
            id=data.get("id"),
            title=data.get("title"),
            content=data.get("content"),
            tags=data.get("tags", []),
            created_at=data.get("created_at")
        )
