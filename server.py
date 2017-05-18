from flask import Flask, request, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from markovtweets import *

app = Flask(__name__)
app.secret_key = "L')BBjpjbJ/uzjm(]v"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return render_template("home.html")


@app.route('/hello_json', methods=["POST"])
def get_username():
    # process username, return JSON
    username = request.form["username"]
    tweet = get_user_tweets(username, count=500)

    data = {"tweet": tweet,
            "username": username
            }
    return jsonify(data)


if __name__ == "__main__":

    app.run(host="0.0.0.0")
