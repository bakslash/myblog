from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'marcus'}
    posts = [
        {
            'author': {'nickname':'john'},
            'body':'Good day in nairobi'
        },
        {
            'author':{'nickname':'susan'},
            'body':'coding is cool'
        }
    ]
          
    return render_template("index.html",
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)
