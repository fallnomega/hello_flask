from flask import Flask

# denotes the name of the file currently being run
app = Flask(__name__)

# python decorator, a decorator is a function thsat gives additional functionality to a function
@app.route('/')
def hello_world():
    #http://127.0.0.1:5000
    return 'Hello World!'

@app.route('/bye')
def say_bye():
    #http://127.0.0.1:5000/bye
    return "Say Goodnight, Gracie!"
if __name__ == '__main__':
    app.run()

# be sure to export and run flask app
# jasonh@local hello_flask > export FLASK_APP=hello.py
# jasonh@local hello_flask > flask run


# decorators

