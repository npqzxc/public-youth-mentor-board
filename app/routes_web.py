from flask import Blueprint, render_template

from app.store import get_record, list_records


web = Blueprint("web", __name__)


@web.get("/")
def dashboard():
    records = list_records()
    return render_template("dashboard.html", title="Youth Mentor Board", records=records)


@web.get("/records")
def records():
    return render_template("records.html", title="Youth Mentor Board", records=list_records())


@web.get("/records/<record_id>")
def detail(record_id: str):
    return render_template("detail.html", title="Youth Mentor Board", item=get_record(record_id))


@web.get("/create")
def create_page():
    return render_template("create.html", title="Youth Mentor Board")
