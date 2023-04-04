from flask import render_template, redirect, request
from flask_app.models.cookie import Cookie
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html", cookies = Cookie.get_all())

# creating a new order
@app.route("/create_order", methods= ["POST"])
def create_order():
    if not Cookie.validate_cookie(request.form):
        return redirect('/neworder')
    data = { 
        'name': request.form['name'],
        'cookietype': request.form['cookietype'],
        'amount': request.form['amount']
    }
    #else
    Cookie.create_order(data)
    return redirect("/")

# New Order Form
@app.route("/neworder")
def form():
    return render_template('neworder.html')

#edit form
@app.route ("/edit/<int:cookie_id>")
def edit (cookie_id):
    return render_template ("edit_order.html", get_order = Cookie.get_one(cookie_id))

@app.route ("/update/<int:cookie_id>", methods =['POST'])
def update(cookie_id):
    if not Cookie.validate_cookie(request.form):
        return redirect('/edit/{cookie_id}')
    data = { 
        "id" : cookie_id,
        'name': request.form['name'],
        'cookietype': request.form['cookietype'],
        'amount': request.form['amount']
    }
    Cookie.update_order(data)
    return redirect("/")
