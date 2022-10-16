from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key ='shh its a secret'

@app.route('/')
def index():
    if 'user' not in session:
        session['user']= 1
    else:
        session['user'] += 1
    return render_template('index.html')

@app.route('/add')
def add():
    session['user'] +=2;
    return redirect ('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
