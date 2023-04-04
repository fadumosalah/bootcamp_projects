from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html", dojos= Dojo.get_all())

#create Dojo
@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data= {
        'name': request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect ("/")

@app.route("/show/<int:id>")
def get_dojo_with_ninjas(id):
    data ={
        "id": id
    }
    return render_template ("show.html", dojo= Dojo.get_dojo_with_ninjas(data) )
