import re
import inspect
from datetime import datetime
from marshmallow import fields, ValidationError, pre_dump, post_load, validates_schema
from flask_marshmallow import Marshmallow
from flask.helpers import url_for
from task_tracker.tracker_rest.api_v1 import models


ma = Marshmallow()

int_regexp = re.compile('^\d{1,10}$')
name_regexp = re.compile('^[a-z_]+$')


# ma.Schema = Schema + jsonify
def extract_cls_attrs(obj, keys):
    mems = inspect.getmembers(obj, lambda f: not inspect.isroutine(f))
    return {a[0]: a[1] for a in mems if a[0] in keys}


# class LoadMixin():
#     def dump_object(self, obj):
#         msg, dm = None, None
#         try:
#             dm = self.load(obj)
#         except ValidationError as err:
#             msg = json.dumps(list(err.messages.values()))
#         finally:
#             return dm, msg

get_time = lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class TaskListInputSchema(ma.Schema):
    name = fields.String(required=True, allow_none=False)
    description = fields.String(required=True, allow_none=False)

    @validates_schema
    def validate_name(self, data, **kwargs):
        if name_regexp.match(data.get('name', '123')) is None:
            raise ValidationError("Name must be latin-alphabetical + '_'")

    @post_load
    def make_tasklist(self, data, **kwargs):
        return models.TaskList(created_dttm=get_time(), **data)


class TaskInputSchema(ma.Schema):
    list_id = fields.Integer(required=True, allow_none=False)
    value = fields.String(required=True, allow_none=False)

    @staticmethod
    def make_task(self, data, list_id=None, **kwargs):
        return models.Task(created_dttm=get_time(), list_id=list_id, **data)


TaskInput = TaskInputSchema()
TasklistInput = TaskListInputSchema()

# --------------------------------------------------------------

class TaskListOutputSchemaHATEOAS(ma.Schema):
    list_id = fields.Integer(required=True, allow_none=False)
    name = fields.String(required=True, allow_none=False)
    description = fields.String(required=True, allow_none=False)
    created_dttm = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    tasks = fields.List(
        fields.URL(relative=True)
    )

    @staticmethod
    def make_tasklist(self, data, list_id=None, **kwargs):
        return models.TaskList(created_dttm=get_time(), **data)

    @pre_dump
    def preprocess(self, data, **kwargs):
        list_i: dict = extract_cls_attrs(data[0][0], models.TaskList.fields)
        tasks_i: list = [url_for('api_v1.task_endpoint',
                                 list_id=list_i['list_id'],
                                 task_id=getattr(row[1], 'task_id'))
                         for row in data]
        d = models.ProxyTasklistHATEOAS(
            tasks=tasks_i,
            **list_i
        )
        return d


class TaskListOutputSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.TaskList
    list_id = fields.Integer(required=True, allow_none=False)
    name = fields.String(required=True, allow_none=False)
    description = fields.String(required=True, allow_none=False)
    created_dttm = fields.DateTime(format='%Y-%m-%d %H:%M:%S')


class TaskOutputSchema(ma.Schema):
    task_id = fields.Integer(required=True, allow_none=False)
    list_id = fields.Integer(required=True, allow_none=False)
    value = fields.String(required=True, allow_none=False)
    created_dttm = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    # is_done - Boolean


TaskListOutput = TaskListOutputSchema()
TaskListHATEOASOutput = TaskListOutputSchemaHATEOAS()
TasksListOutput = TaskListOutputSchema(many=True)

TaskOutput = TaskOutputSchema()
