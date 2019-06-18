from flask import Flask, render_template, url_for,flash,redirect,request
from init import app, db
import os
from sqlalchemy.orm import Session
from forms import RegistrationForm,LoginForm,uRegistrationForm
from models import User


'''posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

'''
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/usermatch",methods=['GET', 'POST'])
def usermatch():
    form = uRegistrationForm()
    return render_template('usermatch.html', title='usermatch', form=form)
    
@app.route('/index')
def index():
   return render_template('index.html')

@app.route("/loginn", methods=['GET', 'POST'])
def loginn():
    
      form = LoginForm()
      return render_template('loginn.html', title='loginn', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    
    return render_template('i.html')

@app.route("/uregister", methods=['GET', 'POST'])
def uregister():                                   
    form = RegistrationForm() # flow of control is from top to bottom; so the logic TO BE PASSED to temp.html is written first, SO THAT it can be passed  okay thanks
    if form.validate_on_submit():

        user = User(name=form.name.data,email=form.email.data,password=form.password.data,spaceused=form.spaceused.data,Location=form.Location.data,price=form.price.data,contact=form.contact.data,address=form.address.data,details=form.details.data)
        db.session.add(user)
        db.session.commit()
        print("validated")
        flash('You were successfully signed up')
        return redirect(url_for('index'))
        
    return render_template('temp.html', title='Register', form=form)
      
@app.route("/pregister", methods=['GET', 'POST'])
def pregister():
    form = RegistrationForm()
    if form.validate_on_submit():

        user = User(name = form.name.data,email=form.email.data,password=form.password.data,details=form.details.data,knownfor=form.knownfor.data,price=form.price.data,contact=form.contact.data)
        db.session.add(user)
        db.session.commit()
        print("validated")
        flash('You were successfully signed up')
        return redirect(url_for('index'))
        
    return render_template('dec.html', title='decregister', form=form)

@app.route("/qregister", methods=['GET', 'POST'])
def qregister():
    form = RegistrationForm()
    if form.validate_on_submit():
           
        user = User(name=form.name.data,email=form.email.data,password=form.password.data,details=form.details.data,knownfor=form.knownfor.data,price=form.knownfor.data,contact=form.contact.data)
        db.session.add(user)
        db.session.commit()
        print("validated")
        print("validated")
        flash('You were successfully signed up')
        return redirect(url_for('index'))

    return render_template('cateror.html', title='catRegister', form=form)
           