from flask_wtf import FlaskForm 
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    
    email = StringField('email', validators=[DataRequired()])
    
    subject = StringField('subject', validators=[DataRequired()])
    
    msg = StringField('msg', validators=[DataRequired()])
    
    