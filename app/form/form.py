from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    author = StringField("Author", validators=[DataRequired()])
    tweet = StringField("Tweet", validators=[DataRequired()])
    submit = SubmitField("Create Tweet")
