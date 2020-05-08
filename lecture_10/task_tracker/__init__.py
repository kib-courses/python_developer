from werkzeug.middleware.dispatcher import DispatcherMiddleware
from task_tracker.tracker_rest import create_app as get_restapp
from task_tracker.tracker_web import create_app as get_webapp


app = DispatcherMiddleware(
    get_restapp(), {'/web': get_webapp()}
)


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, app)
