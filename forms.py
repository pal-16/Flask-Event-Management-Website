from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from flask_login import current_user
from wtforms.validators import DataRequired, Length, Email, EqualTo ,  ValidationError
from models import User


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')      
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo('password')])
    picture = FileField('insert your display Picture', validators=[FileAllowed(['jpg', 'png'])])
    occasion  = StringField('space used for')
    location  = StringField('location')
    price  = StringField('select price range')

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
    price  = StringField('price')
   

    submit = SubmitField('see the match')
                       
class UpdateAccountForm(FlaskForm):
    name = StringField('Username',
                           validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, name):
        if name.data != current_user.name:
            user = User.query.filter_by(name=name.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

           


    
    

