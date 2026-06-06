from flask import Blueprint, jsonify, request

from app.store import create_record, get_record, list_records


api = Blueprint("api", __name__)


@api.get("/dashboard")
def dashboard():
    records = list_records()
    return jsonify(
        {
            "totals": [
                {"label": "总记录", "value": len(records)},
                {"label": "进行中", "value": len([item for item in records if item.status == "进行中"])},
                {"label": "高优先级", "value": len([item for item in records if item.priority == "高"])},
            ],
            "records": [item.__dict__ for item in records],
        }
    )


@api.get("/records")
def records():
    return jsonify([item.__dict__ for item in list_records()])


@api.get("/records/<record_id>")
def record_detail(record_id: str):
    item = get_record(record_id)
    if item is None:
        return jsonify({"error": "not_found"}), 404
    return jsonify(item.__dict__)


@api.post("/records")
def create():
    payload = request.get_json(force=True)
    item = create_record(payload["title"], payload["owner"], payload["note"])
    return jsonify(item.__dict__), 201
