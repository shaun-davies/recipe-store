from recipestore import db


class Cuisine(db.Model):
    # schema for the Cuisine model
    id = db.Column(db.Integer, primary_key=True)
    cuisine_name = db.Column(db.String(30), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="cuisine", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.cuisine_name



class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(30), unique=True, nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisine.id", ondelete="CASCADE"), nullable=False)
    recipe_time = db.Column(db.Integer, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)
    recipe_preparation = db.Column(db.Text, nullable=False)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - Recipe: {self.recipe_name}"