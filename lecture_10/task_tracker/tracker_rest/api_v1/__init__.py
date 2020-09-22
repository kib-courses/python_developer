from sqlalchemy import and_
from sqlalchemy.orm import aliased
from flask import Blueprint, request
from flask_restplus import Api, Resource, fields

import task_tracker.tracker_rest.api_v1.schemas as marshal
from task_tracker.tracker_rest.api_v1.models import db, TaskList as TasklistModel, Task as TaskModel


bp = Blueprint('api_v1', __name__, url_prefix="/api/v1")
api = Api(bp,
          version='v1',
          title='Reminder APIv1',
          description='A simple API v1')


@api.route('/tasklist',
           '/tasklist/<int:list_id>')
class TaskListEndpoint(Resource):
    # /tasklist?contains_task={id|substring}
    def get(self, list_id=None):
        singleton = False

        t = aliased(TaskModel)
        tm = aliased(TasklistModel)
        # data = db.session.query(tm, t).join(t, t.list_id==tm.list_id)

        if list_id:
            singleton = True
            data = db.session.query(tm, t).join(t, t.list_id == tm.list_id).filter(tm.list_id == list_id)
        elif list_id is None and 'contains_task' in request.args:
            task_cond_value = request.args['contains_task']
            if marshal.int_regexp.match(task_cond_value):
                condition = (t.task_id == int(task_cond_value))
            else:
                condition = t.value.ilike(f'%{task_cond_value}%')
            data = db.session.query(tm).join(t, t.list_id==tm.list_id).filter(condition)
        else:
            data = db.session.query(tm)

        res = data.all()
        if len(res) == 0:
            return 'No tasklists'

        if singleton:  # output hateoas
            out = marshal.TaskListHATEOASOutput.dump(res)
        else:
            out = marshal.TasksListOutput.dump(res)
        return out

    def post(self, *args, **kwargs):
        # создать новый список задач
        new_list = marshal.TasklistInput.load(request.get_json())
        if new_list.errors:
            return new_list.errors, 500
        list_row = new_list.data
        db.session.add(list_row)
        db.session.commit()

    def put(self, list_id):
        # обновить список задач
        old_row = db.session.query(TasklistModel).filter(TasklistModel.list_id == list_id).first()
        new_data = marshal.TasklistInput.load(request.get_json())
        if new_data.errors:
            return new_data.errors, 500
        new_row = new_data.data
        if old_row:
            old_row.description = new_row.description
            old_row.created_dttm = new_row.created_dttm
            db.session.add(old_row)
            db.session.commit()
        else:
            return 'NotExists', 404

    def delete(self, list_id):
        # удалить список задач
        db.session.query(TasklistModel).filter(TasklistModel.list_id == list_id).delete()
        db.session.commit()


@api.route('/task/<int:list_id>',
           '/task/<int:list_id>/<int:task_id>')
class TaskEndpoint(Resource):
    """
    /api/task/<int:id>/<int:pos>
    GET - получить задачу $pos из списка $id
    PATCH - обновить задачу $pos из списка $id
    DELETE - удалить задачу $pos из списка $id
    """
    def get(self, list_id, task_id=None):
        if task_id is None:
            # return all by list_id
            data = db.session.query(TaskModel).filter(TaskModel.task_id == task_id)
        else:
            # get specific
            data = db.session.query(TaskModel)
        res = data.all()
        out = marshal.TaskOutput.dump(res)
        return out

    def post(self, list_id, *args, **kwargs):
        # create new task by list_id, return task_id
        new_data = marshal.TaskInput.load(request.get_json())
        if new_data.errors:
            return new_data.errors, 500
        new_row = marshal.TaskInput.make_task(new_data.data, list_id=list_id)
        db.session.add(new_row)
        db.session.commit()

    def delete(self, list_id=None, task_id=None):
        if list_id and task_id is None:
            # delete all by list_id
            delete_pred = db.session.query(TasklistModel).filter(TaskModel.list_id == list_id)
        else:
            # delete specific
            delete_pred = db.session.query(TasklistModel).filter(and_(TaskModel.list_id == list_id,
                                                                      TaskModel.task_id == task_id))
        delete_pred.delete()
        db.session.commit()

    def put(self, list_id, task_id):
        # update specific
        old_row = db.session.query(TaskModel).filter(and_(TaskModel.list_id == list_id,
                                                          TaskModel.task_id == task_id)).first()
        # only if content-type == 'application/json'
        new_data = marshal.TaskInput.load(request.get_json())
        if new_data.errors:
            return new_data.errors, 500
        new_row = marshal.TaskInput.make_task(new_data.data, list_id=list_id)
        if old_row:
            old_row.value = new_row.value
            old_row.created_dttm = new_row.created_dttm
            db.session.add(old_row)
            db.session.commit()
        else:
            return 'NotExists', 404
