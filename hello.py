# from flask import Flask
#
# # denotes the name of the file currently being run
# app = Flask(__name__)
#
# # python decorator, a decorator is a function thsat gives additional functionality to a function
# @app.route('/')
# def hello_world():
#     #http://127.0.0.1:5000
#     return 'Hello World!'
#
# @app.route('/bye')
# def say_bye():
#     #http://127.0.0.1:5000/bye
#     return "Say Goodnight, Gracie!"
# if __name__ == '__main__':
#     app.run()
#
# # be sure to export and run flask app
# # jasonh@local hello_flask > export FLASK_APP=hello.py
# # jasonh@local hello_flask > flask run
#

# decorators
from flask import Flask

app = Flask(__name__)
def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper



def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1> \
           <p>This is my paragraph</p>' \
           '<img src="https://media.giphy.com/media/dCXkBF4WzCTLIkTNYs/giphy.gif">'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def goodbye():
    return 'Bye!'

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"

# # Errors will show up on the webpage since syntax this is right even if the username and name are mismatched.
# @app.route("/<username>")
# def greet(name):
#     return f"Hello {name}!"

# # the debugger pin in the console output can be used on the error page to debug from browser. just click on the
# # console icon that pops up on the debug page and add the pin to start debugging from browser page.
#
# @app.route("/<name>")
# def greet(name):
#     return f"Hello {name + 12}!"

# # You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the
# # <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like
# # <converter:variable_name>.
# @app.route("/username/<path:name>")
# def greet(name):
#     # will return Hello jason/1 + 1 when going to http://127.0.0.1:5000/username/jason/1!
#     return f"Hello {name} + 1!"

# # can also do multiple variables along the path
# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     # will return Hello jason/1 + 1 when going to http://127.0.0.1:5000/username/jason/1!
#     return f"Hello {name}, you are {number} years old!"



if __name__ == "__main__":
    # app.run() Regarding Debug mode, it will allow for autoloading changes in this code without having to restart
    # the app to pull in new code changes.  To enable it, app.run(debug=True) and to load up new changes,
    # save the file and debugger will detect the change and reload. Errors will show up on the webpage.

    # also port 5000 is used by mac so changed the port to 8000 for the app to run on port 8000 locally
    app.run(debug=True, port=8000)


