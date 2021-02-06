from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SubmitInvite(FlaskForm):
    submit = SubmitField('FINISHED')