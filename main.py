from flask import Flask, render_template

import utils as util

app = Flask(__name__)


@app.route('/')
def index():
    title = "Home"
    return render_template("index.html",title=title)

@app.route('/about')
def about():
    title = "About"
    return render_template("about.html",title=title)

@app.route('/team')
def team():
    title = "Team"
    return render_template("team.html",title=title)

@app.route('/contact')
def contact():
    title = "Contact"
    return render_template("contact.html",title=title)

movie_dict = [
              {"title": "Dune", "genre": "Sci-Fi", "rating":2.5},
              {"title": "Alien", "genre": "Sci-Fi", "rating":3.5},
              {"title": "Batman", "genre": "Comics", "rating":4.5}
             ]

movie_dict = util.movie_stars(movie_dict)

@app.route('/movies')
def movies():
  context = {
    "title": "Movies",
    "movies": movie_dict
  }  
  return render_template("movies.html",**context)

app.run(host='0.0.0.0', port=81)
