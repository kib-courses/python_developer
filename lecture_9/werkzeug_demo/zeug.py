import os
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule

# werkzeug.serving.BaseWSGIServer
# TODO - сделать подходящим для Gunicorn

class ProxyAudit(object):
    """Combine multiple applications as a single WSGI application.
    Requests are dispatched to an application based on the path it is
    mounted under.

    :param app: The WSGI application to dispatch to if the request
        doesn't match a mounted path.
    :param mounts: Maps path prefixes to applications for dispatching.
    """

    def __init__(self, app, *args, **kwargs):
        self.app = app

    def __call__(self, environ, start_response):
        print("Incoming transmission :: accessing '%s'" %
              environ.get('REQUEST_URI')
              )
        return self.app(environ, start_response)


class Briefly(object):
    def __init__(self, *args, **kwargs):
        self.glob_value = 'Dawg'

    def dispatch_request(self, request):
        if request.method == 'GET':
            return Response('Yo dawg [%s], I heard you like...' % self.glob_value, status=200)
        elif request.method == 'POST':
            self.glob_value = request.form['name']
            return Response(self.glob_value[::-1], status=200)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(*args, **kwargs):
    app = Briefly()
    n = ProxyAudit(app)
    return n


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5001, app, use_debugger=True, use_reloader=True)
