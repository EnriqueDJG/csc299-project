import json
import os
import uuid

class JSONStorage:
    def __init__(self, directory="./data"):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def _file_path(self, name):
        return os.path.join(self.directory, f"{name}.json")

    def save(self, name, data):
        with open(self._file_path(name), "w") as f:
            json.dump(data, f, indent=4)

    def load(self, name):
        path = self._file_path(name)
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            return json.load(f)

    def generate_id(self):
        return str(uuid.uuid4())
