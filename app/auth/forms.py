from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), Email("Некоректный email")])
    psw = PasswordField("Password: ",
                        validators=[DataRequired(),
                                    Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")])
    remember = BooleanField("Remember? ", default=False)
    submit = SubmitField("Enter")
