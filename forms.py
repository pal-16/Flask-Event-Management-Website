from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo ,  ValidationError
from models import User

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
    
    occasion  = StringField('space used for')
    location  = StringField('location')
    price  = StringField('price', validators=[DataRequired()])
   
    contact  = StringField('contact', validators=[DataRequired()])
    address  = StringField('address')
    requirement =SelectField('requirement',
                        validators=[DataRequired()],choices=[('h','halls'),('d','decorators'),('c','cateorors')])
    


    submit = SubmitField('Sign Up')

    def validate_username(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

   

class uRegistrationForm(FlaskForm):
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
   
    requirement  = SelectField('requirement',
                        validators=[DataRequired()],choices=[('h','halls'),('d','decorators'),('c','cateorors')])
    location  = StringField('location',
                        validators=[DataRequired()])
    price  = StringField('price',
                        validators=[DataRequired()])
  
   

    submit = SubmitField('see the match')
                       

           


    
    

