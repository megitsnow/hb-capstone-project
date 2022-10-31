"""Server for movie ratings app."""

from flask import Flask
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import os
# from model import connect_to_db, db


from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """Returns homepage."""

    return render_template('index.html')

@app.route("/drivers")
def all_drivers():
    """View all movies."""

    return render_template("index.html")

@app.route("/constructors")
def all_constructors():
    """View all movies."""

    return render_template("index.html")

@app.route("/recent_news")
def recent_news():
    """View all movies."""

    return render_template("index.html")

@app.route("/logo_data")
def fetch_logo_data():
    """View all movies."""
    arr = os.listdir('./static/imgs/constructors')
    logo_photos = []

    for item in arr:
        item = "/static/imgs/constructors/" + item
        logo_photos.append(item)

    return jsonify(logo_photos)



if __name__ == "__main__":
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)