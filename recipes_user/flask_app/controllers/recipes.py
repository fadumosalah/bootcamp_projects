from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.recipe import Recipe

# recipe form
@app.route("/newrecipe")
def newcar():
    if "user_id" not in session:
        return redirect ('/')
    return render_template('new_recipe.html')

# adding recipe

@app.route('/create_recipe',methods=['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect("/newrecipe")
    data ={
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "date_cooked" : request.form["instructions"],
        "minutes" : request.form["minutes"],
        "user_id" : session["user_id"],
    }
    Recipe.create_recipe(data)
    return redirect('/dashboard')

@app.route('/showrecipe/<int:recipe_id>')
def show_recipe(recipe_id):
    data ={
        "id" : recipe_id
    }
    recipe = Recipe.get_recipe(data)
    return render_template("show.html", recipe= recipe)

@app.route ('/editrecipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    data ={
        "id" : recipe_id
    }
    recipe = Recipe.get_recipe(data)
    return render_template("edit.html", recipe= recipe)

@app.route ('/updaterecipe/<int:recipe_id>', methods =["POST"])
def updaterecipe(recipe_id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/updaterecipe/{recipe_id}")
    Recipe.updaterecipe(request.form, recipe_id)
    return redirect ('/dashboard')

@app.route("/deleterecipe/<int:recipe_id>")
def deleterecipe (recipe_id):
    data ={
        "id" : recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect ('/dashboard')