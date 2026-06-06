from dataclasses import dataclass


@dataclass
class Record:
    record_id: str
    title: str
    owner: str
    status: str
    priority: str
    note: str
