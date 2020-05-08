# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html#building-a-relationship
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
# https://docs.sqlalchemy.org/en/13/orm/cascades.html#cascades

class TaskList(db.Model):
    __tablename__ = 'tasklists'
    fields = {'list_id', 'name', 'description', 'created_dttm'}

    list_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    created_dttm = Column(DateTime)
    task = relationship("Task", back_populates="tasklist")

    def __init__(self, name=None, description=None, created_dttm=None):
        self.name = name
        self.description = description
        self.created_dttm = created_dttm


class Task(db.Model):
    __task__ = 'tasks'
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    list_id = Column(Integer, ForeignKey('tasklists.list_id', ondelete='CASCADE'))
    value = Column(String)
    created_dttm = Column(DateTime)
    tasklist = relationship("TaskList", back_populates="task")

    def __init__(self, list_id=None, value=None, created_dttm=None):
        self.list_id = list_id
        self.value = value
        self.created_dttm = created_dttm


class ProxyTasklistHATEOAS:
    def __init__(self, tasks=None, **kwargs):
        self.tasks = tasks
        for k,v in kwargs.items():
            setattr(self, k, v)
