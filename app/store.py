import json
from pathlib import Path

from app.models import Record
from app.seed import default_records


DATA_FILE = Path("data/records.json")


def ensure_data_file() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text(
            json.dumps([record.__dict__ for record in default_records()], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def list_records() -> list[Record]:
    ensure_data_file()
    payload = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return [Record(**item) for item in payload]


def get_record(record_id: str) -> Record | None:
    for item in list_records():
      if item.record_id == record_id:
        return item
    return None


def create_record(title: str, owner: str, note: str) -> Record:
    records = list_records()
    record = Record(f"r{len(records) + 1}", title, owner, "新建", "中", note)
    payload = [record.__dict__] + [item.__dict__ for item in records]
    DATA_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return record
