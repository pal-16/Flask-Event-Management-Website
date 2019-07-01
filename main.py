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

@app.route("/home",methods=['GET', 'POST'])
def home():
    form = uRegistrationForm()
    if form.validate_on_submit():
        print("success1")
        return redirect(url_for('find',location=form.location.data,price=form.price.data,requirement=form.requirement.data))
    return render_template('usermatch.html', title='home', form=form)

'''@app.route('/list')
def list():
    users = User.query.all()
    return render_template('list.html',title='list', myUsers=users)'''


    
@app.route('/index')
def index():
   return render_template('index.html')

'''@app.route('/find/<email>')
def findUser(email):
    user = User.query.filter_by(email=email).first()
    return render_template('detail.html', myUser=user)'''

@app.route('/find',methods=['GET', 'POST'])
def find():
    form = uRegistrationForm()
    user = User.query.filter_by(location=form.location.data,price=form.price.data,requirement=form.requirement.data)
    if user :                     
      print("success2")                                                    # this part is getting executed!!!!!
    return render_template('detail.html',title='match',form=form,user=user)
    

   
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

        user = User(name=form.name.data,email=form.email.data,password=form.password.data,occasion=form.occasion.data,location=form.location.data,price=form.price.data,contact=form.contact.data,address=form.address.data,requirement=form.requirement.data)
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

        user = User(name = form.name.data,email=form.email.data,password=form.password.data,requirement=form.requirement.data,price=form.price.data,contact=form.contact.data)
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
                      
        user = User(name=form.name.data,email=form.email.data,password=form.password.data,requirement=form.requirement.data,price=form.requirement.data,contact=form.contact.data)
        db.session.add(user)
        db.session.commit()
        print("validated")
        print("validated")
        flash('You were successfully signed up')
        return redirect(url_for('index'))
           
    return render_template('cateror.html', title='catRegister', form=form)
