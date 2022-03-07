from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# @app.route('/')
@app.route('/hello', methods=['POST', 'GET'])

# def hello_world():
#     greeting = "Azure SDK"
#     return f'Hello, {greeting}!'

# def index():
#     greeting = "Azure SDK"
#     return render_template("index.html", greeting=greeting)

def index():

    # name = request.args.get('name', 'Nobody')
    # http://127.0.0.1:5000/hello?name=

    # greet = request.args.get('greet', 'Hello')
    # http://127.0.0.1:5000/hello?name=&greet=

    # if name:
    #     greeting = f"{greet}, {name}"
    # else:
    #     greeting = "Hellow Azure SDK"

    # return render_template("index.html", greeting=greeting)

    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")

if __name__ == "__main__":
    app.run()