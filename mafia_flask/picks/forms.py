from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from sportsreference.nfl.boxscore import Boxscores


class PickForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    pick1 = RadioField('Choose Winner', validators=[DataRequired()], choices=[
                       ('patriots', 'Patriots'), ('jets', 'Jets')])
    pick2 = RadioField('Choose Winner 2', validators=[DataRequired()], choices=[
        ('ravens', 'Ravens'), ('browns', 'Browns')])
    pick3 = RadioField('Choose Winner 3', validators=[DataRequired()], choices=[
        ('ravens', 'Ravens3'), ('browns', 'Browns3')])
    pick5 = RadioField('Choose Winner 4', validators=[DataRequired()], choices=[
        ('ravens', 'Ravens4'), ('browns', 'Browns4')])
    submit = SubmitField('Post')
