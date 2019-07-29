from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c8ca7a149fbc2248095f13968c84d6bd'   # string manually generated from secrets.hex_token(16)

posts = [
    {
        'author': 'Durga Sahoo',
        'title': 'Blog Post 1',
        'content': 'First post content...',
        'date_posted': 'Jul 21, 2019'
    },
    {
        'author': 'Deepu S',
        'title': 'Blog Post 2',
        'content': 'Second post content...',
        'date_posted': 'Jul 22, 2019'
    }
]


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
