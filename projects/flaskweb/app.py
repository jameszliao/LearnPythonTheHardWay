from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

# def hello_world():
#     greeting = "Azure SDK"
#     return f'Hello, {greeting}!'

def index():
    greeting = "Azure SDK"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()