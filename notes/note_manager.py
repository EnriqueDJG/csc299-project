from storage.json_storage import JSONStorage

class NoteManager:
    def __init__(self, storage: JSONStorage):
        self.storage = storage
        self.storage_key = "notes"

    def create_note(self, title, content, tags=None):
        notes = self.storage.load(self.storage_key)

        note = {
            "id": self.storage.generate_id(),
            "title": title,
            "content": content,
            "tags": tags or []
        }

        notes.append(note)
        self.storage.save(self.storage_key, notes)
        return note

    def search_notes(self, keyword):
        notes = self.storage.load(self.storage_key)
        keyword = keyword.lower()
        return [
            n for n in notes
            if keyword in n["title"].lower() or keyword in n["content"].lower()
        ]

    def delete_note(self, note_id):
        notes = self.storage.load(self.storage_key)
        notes = [n for n in notes if n["id"] != note_id]
        self.storage.save(self.storage_key, notes)
