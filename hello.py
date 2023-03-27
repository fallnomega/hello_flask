from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# be sure to export and run flask app
# jasonh@local hello_flask > export FLASK_APP=hello.py
# jasonh@local hello_flask > flask run
