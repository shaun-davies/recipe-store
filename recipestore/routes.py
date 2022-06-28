from flask import render_template, request, redirect, url_for
from recipestore import app, db
from recipestore.models import Cuisine, Recipe


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/cuisines")
def cuisines():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    return render_template("cuisines.html", cuisines=cuisines)


@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        cuisine = Cuisine(cuisine_name=request.form.get("cuisine_name"))
        db.session.add(cuisine)
        db.session.commit()
        return redirect(url_for("cuisines"))
    return render_template("add_cuisine.html")
