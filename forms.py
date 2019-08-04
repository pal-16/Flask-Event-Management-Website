from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.fields.html5 import EmailField

from flask_login import current_user
from wtforms.validators import DataRequired, Length, Email, EqualTo ,  ValidationError
from models import Org,User


class LoginForm(FlaskForm):
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')      
    submit = SubmitField('Login')


class dynamicForm(FlaskForm):
    price  = StringField('select price range')
    location  = StringField('location')
    remember = BooleanField('Remember Me')      
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    name = StringField(' hall name', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo('password')])
    
    occasion  = StringField('space used for')
    location  = SelectField('location',choices=[('a','andheri'),('b','borivali'),('c','churchgate'),('d','dadar'),('g','ghatkopar'),('j','jogeshwari'),('k','kandivali'),('l','lowerparel'),('n','nerul'),('p','parel'),('s','santacruz')])
    price  = StringField('enter the price range')

    contact  = StringField('contact', validators=[DataRequired()])
    address  = StringField('address')
    #requirement =SelectField('requirement', validators=[DataRequired()],choices=[('h','halls')])
    submit = SubmitField('Sign Up')

class dRegistrationForm(FlaskForm):
    name = StringField(' hall name', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo('password')])
    
    
    price  = StringField('enter the price range')

    contact  = StringField('contact', validators=[DataRequired()])
    
    requirement =SelectField('requirement',
                        validators=[DataRequired()],choices=[('d','decorators')])
 
    submit = SubmitField('Sign Up')


class cRegistrationForm(FlaskForm):
    name = StringField(' hall name', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo('password')])
    
    
    
    price  = StringField('enter the price range')

    contact  = StringField('contact', validators=[DataRequired()])
   
    requirement =SelectField('requirement',
                        validators=[DataRequired()],choices=[('c','cateorors')])
 
    submit = SubmitField('Sign Up')





class planRegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo('password')])
    
    special=StringField('specialization for', validators=[DataRequired()])
    requirement =SelectField('requirement',
                        validators=[DataRequired()],choices=[('p','party planners')])
 

    submit = SubmitField('Sign Up')

   
class uRegistrationForm(FlaskForm):
    
    #email = EmailField('Email address', validators=[DataRequired(), Email()])
   
    requirement  = SelectField('requirement',
                        choices=[('h','halls'),('d','decorators'),('c','cateorors')])
    location  = SelectField('location',choices=[('a','andheri'),('b','borivali'),('c','churchgate'),('d','dadar'),('g','ghatkopar'),('j','jogeshwari'),('k','kandivali'),('l','lowerparel'),('n','nerul'),('p','parel'),('s','santacruz')])
    price  = StringField('price')
   

    submit = SubmitField('see the match')

    

   
                       
class UpdateAccountForm(FlaskForm):
    name = StringField('Username',
                           validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
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

class InviteForm(FlaskForm):         
          invite = SubmitField('Invite')


    
    

