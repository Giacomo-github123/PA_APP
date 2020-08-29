#Here we are importing the Flask class from flask
from flask import Flask, flash, redirect
from flask import render_template
from flask import url_for
from forms import RegistrationForm, LoginForm

#app is a class instance of Flask
#the __name__ is a special variable which means the module
app = Flask(__name__)
app.config['SECRET_KEY'] = '40debbc1a1d5ad11c43ec02e0618e97b'

posts = [
    {
        'author'      : 'Giacomo Sotti',
        'title'       : 'Blog Post Test',
        'content'     : 'First Post',
        'date_posted' : 'July 30, 2020'
    },
    {
        'author'      : 'Giulio Sotti',
        'title'       : 'Blog Post Test 2',
        'content'     : 'Second Post',
        'date_posted' : 'July 30, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods = ['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Accout Created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Sign Up', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    app.run(debug = True)