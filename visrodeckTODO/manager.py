from .task import Task
from .storage import JSONStorage
from .utils import generate_id, get_now_iso

class TaskManager:
    def __init__(self):
        self.storage = JSONStorage()
        self.tasks = [Task.from_dict(t) for t in self.storage.load()]

    def save(self):
        self.storage.save([t.to_dict() for t in self.tasks])

    def add_task(self, title, description, due_date, priority):
        now = get_now_iso()
        task = Task(
            id=generate_id(),
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status="pending",
            created_at=now,
            updated_at=now
        )
        self.tasks.append(task)
        self.save()
        return task

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save()

    def update_task(self, task_id, **kwargs):
        for t in self.tasks:
            if t.id == task_id:
                for key, value in kwargs.items():
                    if hasattr(t, key):
                        setattr(t, key, value)
                t.updated_at = get_now_iso()
                break
        self.save()

    def get_all(self):
        return self.tasks

    def get_completed(self):
        return [t for t in self.tasks if t.status == "completed"]

    def get_pending(self):
        return [t for t in self.tasks if t.status == "pending"]
