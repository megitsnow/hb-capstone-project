"""Server for movie ratings app."""

from flask import Flask
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import os
from datetime import datetime
import requests


from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ["NEWS_API_KEY"]
TODAY = datetime.today()
DATE = TODAY.strftime("%y-%m-%d")


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
    """View all constructors."""

    return render_template("index.html")

@app.route("/recent_news")
def recent_news():
    """View recent news."""

    return render_template("index.html")

@app.route("/recent_news_data")
def get_recent_news():
    """Get recent news data"""
    url = ('https://newsapi.org/v2/everything?'
    'q=Apple&'
    'from=2022-10-31&'
    'sortBy=popularity&'
    'apiKey=ee29418291e04bc5b28d1f2c719cb218')
    response = requests.get(url)
    
    

    return jsonify(articles)

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