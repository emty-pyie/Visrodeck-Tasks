from dataclasses import dataclass, asdict

@dataclass
class Task:
    id: str
    title: str
    description: str
    due_date: str
    priority: str
    status: str
    created_at: str
    updated_at: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
