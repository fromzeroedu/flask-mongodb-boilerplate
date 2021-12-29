from application import db


class Counter(db.Document):  # type: ignore
    count = db.IntField(db_field="c")
