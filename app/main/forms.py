from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class UserForm(Form):
    username = StringField(
        validators=[
            DataRequired("Can not be empty"),
        ],
        render_kw={
            "placeholder": "Please enter your username",
        }
    )
    password = PasswordField(
        validators=[
            DataRequired("Can not be empty")
        ],
        render_kw={
            "placeholder": "Please enter your password",
        }
    )
    submit = SubmitField('Submit')


class LoginForm(Form):
    username = StringField(
        validators=[
            DataRequired("Can not be empty"),
        ],
        render_kw={
            "placeholder": "Please enter your username",
        }
    )
    password = PasswordField(
        validators=[
            DataRequired("Can not be empty")
        ],
        render_kw={
            "placeholder": "Please enter your password",
        }
    )
    submit = SubmitField('Login')
