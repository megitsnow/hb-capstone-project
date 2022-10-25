"""Server for movie ratings app."""

from flask import Flask
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """Returns homepage."""

    return render_template('homepage.html')

@app.route("/movies")
def all_movies():
    """View all movies."""

    movies = crud.show_movies()

    return render_template("all_movies.html", movies=movies)

@app.route("/movies/<movie_id>")    
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)
    
    return render_template("movie_details.html", movie = movie)

@app.route("/users")
def all_users():
    """View all users."""

    users = crud.show_users()

    return render_template("all_users.html", users=users)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form["email"]
    password = request.form["password"]

    if crud.get_user_by_email(email) == None:
        new_user = crud.create_user(email, password)
        db.session.add(new_user)
        db.session.commit()
        flash("Success! You can now log in!")
    else:
        flash("You can't create an account with that email, account already exists")

    return redirect("/")

@app.route("/users/<user_id>")    
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)
    
    return render_template("user_details.html", user = user)  

@app.route("/login", methods=["POST"])
def login():
    """Log in a user."""

    email = request.form["email"]
    password = request.form["password"]

    user = crud.get_user_by_email(email)

    if user == None or user.password != password:
        flash("Login unsuccessful! Please try again.")
        return redirect("/")
    else:
        session['user'] = user.user_id
        flash("Logged in!")
        return redirect("/movies")

@app.route("/movie/<movie_id>/ratings", methods=["POST"])
def create_rating(movie_id):
    """Create a rating for a movie."""
    user = crud.get_user_by_id(session["user"])
    movie = crud.get_movie_by_id(movie_id)
    rating = int(request.form["rating"])

    new_rating = crud.create_rating(user, movie , rating)
    db.session.add(new_rating)
    db.session.commit()

    return redirect("/movies")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)