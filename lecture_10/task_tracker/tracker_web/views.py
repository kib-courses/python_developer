from flask import Blueprint, request, render_template


bp = Blueprint('web', __name__,
               static_folder="static",
               template_folder="templates"
               )


@bp.route('/home')
def homepage():
    return render_template('base.html')
