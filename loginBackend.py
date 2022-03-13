from flask import Flask, request, render_template
# from wtforms import Form, StringField, TextAreaField, PasswordField, validators

app = Flask(__name__)

# Hardcoded User (Because we can't use a regular database)
User = {
    "username": "root",
    "email": "root@example.com",
    "password": "123456"
}


# Class for registration
# class RegisterForm(Form):
#     username = StringField('Username', [validators.Length(min=4, max=25)])
#     email = StringField('Email', [validators.Length(min=6, max=50)])
#     password = PasswordField('Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords do not match')
#     ])
#     confirm = PasswordField('Confirm Password')

@app.route('/')
def my_form():
    return render_template('login.html')

# User Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm(request.form)
#     if request.method == 'POST' and form.validate():
#         name = form.name.data
#         email = form.email.data
#         username = form.username.data
#         password = sha256_crypt.encrypt(str(form.password.data))

#         return redirect(url_for('login'))
#     return render_template('register.html', form=form)


# User login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form.get("username")
        password = request.form.get("password")
        # Check if this matches the "user" dictionary
        print(username, User.get("username"))
        print(password, User.get("password"))
        if username == User.get("username") and password == User.get("password"):
            error = 'Login Successful'
            return render_template('login.html', error=error)
        else:
            error = 'User not found'
            return render_template('login.html', error=error)
    return render_template('login.html')
