from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class promptForm(FlaskForm):
    prompt = StringField(label="prompt", validators=[DataRequired()])
