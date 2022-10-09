from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
  user = {"username": "Cattleya"}
  posts = [
    {
      "author": {"username": "Juan"},
      "body": "Our life is the creation of our mind."
    },
    {
      "author": {"username": "Ayya"},
      "body": "Everything is mind-made."
    }
  ]
  return render_template("index.html", title="Home", user=user, posts=posts)