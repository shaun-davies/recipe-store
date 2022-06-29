from flask import render_template, request, redirect, url_for
from recipestore import app, db
from recipestore.models import Cuisine, Recipe


@app.route("/")
def home():
    recipes = list(Recipe.query.order_by(Recipe.id).all())
    return render_template("base.html", recipes=recipes)


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


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            cuisine_id=request.form.get("cuisine_id"),
            recipe_time=request.form.get("recipe_time"),
            recipe_ingredients=request.form.get("recipe_ingredients"),
            recipe_preparation=request.form.get("recipe_preparation")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_recipe.html", cuisines=cuisines)


@app.route("/view_recipe/<int:recipe_id>", methods=["GET"])
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("view_recipe.html", recipe=recipe)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name")
        recipe.cuisine_id = request.form.get("cuisine_id")
        recipe.recipe_time = request.form.get("recipe_time")
        recipe.recipe_ingredients = request.form.get("recipe_ingredients")
        recipe.recipe_preparation = request.form.get("recipe_preparation")
        db.session.commit()
    return render_template("edit_recipe.html", recipe=recipe, cuisines=cuisines)


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home"))