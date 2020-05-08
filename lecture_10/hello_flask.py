from flask import Flask
from werkzeug.serving import run_simple

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    run_simple('localhost', 5000, app)
