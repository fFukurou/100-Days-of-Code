from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper_function(*args, **kwargs):
        text = function()
        return f"<b>{text.upper()}By: Lea!</b>"
    return wrapper_function




@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello World </h1> '\
    '<p>This is a paragraph</p>'\
    '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDViZDVyd2VvZWJqdXZoZTFraXg0eGU2eW1kcHQwbjh2M25majh6byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.webp" '\
    'alt="Cat kissing camera"/>'\
    ''


@app.route('/bye')
@make_bold
def bye():
    return "bye!"

@app.route('/username/<name>')
def greet(name):
    return f"Hello {name}."


@app.route('/username/<name>/<int:number>')
def greet_age(name, number):
    return f"Hello {name}, you are {number} years old..."



if __name__ == "__main__":
    app.run(debug=True)


