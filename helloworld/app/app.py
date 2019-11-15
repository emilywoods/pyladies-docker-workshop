import os
from flask import Flask, render_template

app = Flask(__name__)

NAME = os.environ.get("NAME", "World")

@app.route("/")
def homepage():
    return render_template("index.html", username=NAME)


if __name__ == "__main__":

    app.run(host="0.0.0.0")

