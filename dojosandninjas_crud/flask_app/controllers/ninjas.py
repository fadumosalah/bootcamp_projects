from flask import render_template, redirect, request
from flask_app.models import ninja
from flask_app.models.dojo import Dojo
from flask_app.controllers import dojos
from flask_app import app

@app.route ("/addninja")
def add_ninja():
    return render_template ("newninja.html", dojos= Dojo.get_all())

#creating a ninja under a dojo
@app.route ("/create_ninja", methods =["POST"])
def create_ninja():
    data = {
        'dojo_id' : request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    ninja.Ninja.create_ninja(data)
    return redirect ("/")