from sqlalchemy.orm.attributes import InstrumentedAttribute
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from py.appbase.database import db
from py.models import CommonColumnsMixin, set_attributes_from_dict


class TaskGroup(CommonColumnsMixin, db.Model):
    task_group_id = db.Column(db.Integer, primary_key=True)
    task_group_title = db.Column(db.String(200), unique=False)

    tasks = db.relationship('Task', backref='task_group', lazy=True)


class Task(CommonColumnsMixin, db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(200), unique=False)
    task_detail = db.Column(db.Text, unique=False)
    status = db.Column(db.String(30))
    deadline = db.Column('deadline', db.DATETIME, nullable=True)

    task_group_id = db.Column('task_group_id', db.Integer, db.ForeignKey('task_group.task_group_id'))

    def __init__(self, task: dict):
        set_attributes_from_dict(self, task)

    def __repr__(self):
        return '<Task %r, %s>' % (self.task_id, self.title)
