from flask import render_template
from recipestore import app, db
from recipestore.models import Cuisine, Recipe


@app.route("/")
def home():
    return render_template("base.html")