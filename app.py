from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb://localhost:27017/")  
db = client["recipeDB"]
recipes = db["recipes"]

@app.route("/")
def index():
    all_recipes = recipes.find()
    return render_template("index.html", recipes=all_recipes)

@app.route("/add", methods=["POST"])
def add_recipe():
    title = request.form.get("title")
    ingredients = request.form.get("ingredients")
    steps = request.form.get("steps")
    time = request.form.get("time")

    recipes.insert_one({
        "title": title,
        "ingredients": ingredients,
        "steps": steps,
        "time": time
    })
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
