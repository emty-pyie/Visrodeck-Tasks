import json
import os

class JSONStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks_data):
        with open(self.filename, 'w') as f:
            json.dump(tasks_data, f, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
