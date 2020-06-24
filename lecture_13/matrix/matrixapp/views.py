import sys
import inspect
from flask import Blueprint

import matrixapp.actors as actors

bp = Blueprint('matrix', __name__, url_prefix='/')

class_map = {cls.msg_id: cls()
    for cls_name, cls in inspect.getmembers(actors, inspect.isclass)
    if cls.msg_id
}


@bp.route('/<actor_id>')
@bp.route('/<actor_id>/meets/<companion>')
def main_view(actor_id, companion=None):
    if actor_id in class_map:
        if not companion:
            return str(class_map[actor_id])
        else:
            return class_map[actor_id].interact(class_map[companion])
    else:
        return 404, 'Actor not found'
