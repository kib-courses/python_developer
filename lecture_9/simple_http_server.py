from http.server import HTTPServer, SimpleHTTPRequestHandler

#1 https://docs.python.org/3/library/http.server.html
#2 https://github.com/python/cpython/blob/3.8/Lib/http/server.py
#3 https://github.com/python/cpython/blob/cc011b5190b63f0be561ddec38fc4cd9e60cbf6a/Lib/socketserver.py#L390

# From #3.L262
# The distinction between handling, getting, processing and finishing a
# request is fairly arbitrary.  Remember:
#
# - handle_request() is the top-level call.  It calls selector.select(),
#   get_request(), verify_request() and process_request()
# - get_request() is different for stream or datagram sockets
# - process_request() is the place that may fork a new process or create a
#   new thread to finish the request
# - finish_request() instantiates the request handler class; this
#   constructor will handle the request all by itself

PORT = 8080
ADDR = 'localhost'


# SimpleHTTPRequestHandler отнаследован от StreamRequestHandler
class PimpHandler(SimpleHTTPRequestHandler):
    HTML = "<html><body><h1>Yo dawg %s</h1></body></html>"

    def set_header(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

    def do_GET(self) -> None:
        self.set_header()
        self.wfile.write(
            (self.HTML % self.path.strip().replace('/', '')).encode()
        )


httpd = HTTPServer((ADDR, PORT), PimpHandler)
httpd.serve_forever()
