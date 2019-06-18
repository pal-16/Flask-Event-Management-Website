from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

'''
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
'''

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
            
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo('password')])
    
    spaceused  = StringField('space used for')
    Location  = StringField('location')
    price  = StringField('price', validators=[DataRequired()])
   
    contact  = StringField('contact', validators=[DataRequired()])
    address  = StringField('address')
    details = StringField('details', validators=[DataRequired()])
    knownfor = StringField('knownfor')


    submit = SubmitField('Sign Up')

class uRegistrationForm(FlaskForm):
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
   
    requirement  = StringField('requirement',
                        validators=[DataRequired()])
    occasion  = StringField('occasion',
                        validators=[DataRequired()])
  
   

    submit = SubmitField('see the match')
                       

    

