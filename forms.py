from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.fields.html5 import EmailField

from flask_login import current_user
from wtforms.validators import DataRequired, Length, Email, EqualTo ,  ValidationError
from models import Org,User


class LoginForm(FlaskForm):
    email = EmailField('Email address:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember = BooleanField('Remember Me?')      
    submit = SubmitField('Login')


class dynamicForm(FlaskForm):
    price  = StringField('Change price range:')
    location  = StringField(' Change location:')
    remember = BooleanField('Remember Me?')
    submit = SubmitField('Login')

class hRegistrationForm(FlaskForm):
    name = StringField('Hall name:', validators=[DataRequired()])
    email = EmailField('Email address:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password:',
                                     validators=[EqualTo('password')])
    
    occasion  = StringField('Events hosted:')
    location  = SelectField('Location:',choices=[('a','Andheri'),('z','any'),('b','Borivali'),('c','Churchgate'),('d','Dadar'),('g','Ghatkopar'),('k','Kandivali'),('n','Nerul'),('s','Santacruz')])
    price  = StringField('Approximate Budget Limit:', validators=[DataRequired()])
    details  = StringField('Details:', validators=[DataRequired()])
    accomodation = StringField('Accomodation Capacity:')
    contact  = StringField('Contact:', validators=[DataRequired()])
    address  = StringField('address')
    requirement =SelectField('requirement', validators=[DataRequired()],choices=[('h','halls')])
    submit = SubmitField('Sign Up')
   ## def validate_email(self, email):
       # if email.data != current_user.email:
          #  user = Org.query.filter_by(email=email.data).first()
         #   if user:
             #   raise ValidationError('That email is taken. Please choose a different one.')


class dRegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo('password')])
    
    
    price  = StringField('Approximate Budget Limit:', validators=[DataRequired()])
 

    contact  = StringField('Contact:', validators=[DataRequired()])
    details  = StringField('Details:', validators=[DataRequired()])
    
    requirement =SelectField('Requirement:',
                        validators=[DataRequired()],choices=[('d','decorators')])
 
    submit = SubmitField('Sign Up')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class cRegistrationForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email address:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password:',
                                     validators=[EqualTo('password')])
    price  = StringField('Approximate Budget Limit:')
    contact  = StringField('Contact:', validators=[DataRequired()])
    requirement =SelectField('Requirement:',
                        validators=[DataRequired()],choices=[('c','caterers')])
    details  = StringField('Details:', validators=[DataRequired()])
    
    submit = SubmitField('Sign Up')
   



class planRegistrationForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email address:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password:',
                                     validators=[EqualTo('password')])
    
    special=StringField('Known for', validators=[DataRequired()])
    details=StringField('Details:', validators=[DataRequired()])
    requirement =SelectField('Requirement:',
                        choices=[('p','party planners')])
 
    price  = StringField('Approximate Budget Limit:')

    contact  = StringField('Contact:', validators=[DataRequired()])
   
    submit = SubmitField('Sign Up')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = Org.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

   
class uRegistrationForm(FlaskForm):
    requirement  = SelectField('Requirement:',
                        choices=[('h','halls'),('d','decorators'),('c','caterers'),('p','partyplanners')])
    location  = SelectField('Location:',choices=[('a','Andheri'),('z','any'),('b','Borivali'),('c','Churchgate'),('d','Dadar'),('g','Ghatkopar'),('k','Kandivali'),('n','Nerul'),('s','Santacruz')])    
    price  = StringField('Approximate Budget Limit:')
    submit = SubmitField('Search')


class UpdateAccountForm(FlaskForm):

    name = StringField(' hall name', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
             
             
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, name):
        if name.data != current_user.name:
            user = Org.query.filter_by(name=name.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Org.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


    
    

