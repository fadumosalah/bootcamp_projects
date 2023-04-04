import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ='shh its a secret'

@app.route('/')
def game():
    if 'goal' not in session:
        session['goal'] = 0
    return render_template ('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
    if request.form['gold'] == 'farm':
        session['goal'] += random.randint(10,20);
    elif request.form['gold'] == 'cave':
        session['goal'] += random.randint(5,10)
    elif request.form['gold'] == 'house':
        session['goal'] += random.randint(0,50)
    elif request.form['gold'] == 'casino':
        gamble = random.randint(-50,50)
        session['goal'] += gamble;
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)