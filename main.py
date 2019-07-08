import os
import secrets
from PIL import Image
from flask import Flask,session, render_template, url_for,flash,redirect,request
from init import app, db , bcrypt
import os
from sqlalchemy.orm import Session
from flask_bcrypt import (Bcrypt,
                          check_password_hash,
                          generate_password_hash,)

from forms import RegistrationForm,LoginForm,uRegistrationForm,UpdateAccountForm
from models import User
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy_utils import IntRangeType


def create_session(config):
    engine = create_engine(config['DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session 
    
@app.route("/")
@app.route("/home",methods=['GET', 'POST'])
def home():
    form = uRegistrationForm()
    if form.validate_on_submit():
        print("success1")
        print("user details stored") # this is not getting printed, for sure
        return redirect(url_for('find'))
    return render_template('usermatch.html', title='home', form=form)

@app.route("/display")
def display():
    return render_template('detail.html')

@app.route('/index')
def index():
   return render_template('index.html')


@app.route('/flas')
def flas():
   return render_template('flas.html')


@app.route('/find',methods=['GET', 'POST'])
def find():
    form = uRegistrationForm()

    user = User.query.filter_by(location=form.location.data,requirement=form.requirement.data).all()
    if user:                     
      print("success2") # this is working   
      return render_template('detail.html',title='match',form=form,user=user)
      print("okay")
      
      if user1:
        return render_template('detail.html',title='match',form1=form,user=user)

    else:
        return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print("good")
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print("palak")
            login_user(user, remember=form.remember.data)

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash('Login Unsuccessful. Please check email and password')
            return redirect(url_for('flas'))
    return render_template('login.html', title='Login', form=form)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static', 'profile_pics', picture_fn)
    print('Picture to be saved: ', picture_path)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/logout")
def logout():
    logout_user()
    return render_template('logout.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    
    return render_template('i.html')

@app.route("/hregister", methods=['GET', 'POST'])
def uregister():                                   
    form = RegistrationForm() # flow of control is from top to bottom; so the logic TO BE PASSED to temp.html is written first, SO THAT it can be passed  okay thanks
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        user = User(name=form.name.data,email=form.email.data,password=hashed_password,location=form.location.data,price=form.price.data,contact=form.contact.data,address=form.address.data,requirement=form.requirement.data)

        if form.picture.data: 
            image_file = save_picture(form.picture.data)
            user.image_file = url_for('static', filename='profile_pics/'+user.image_file)
            print('Profile picture saved')

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
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
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
        if form.picture.data:
            picture_file = save_picture(form.picture.data)           
        user = User(name=form.name.data,email=form.email.data,password=form.password.data,requirement=form.requirement.data,price=form.price.data,contact=form.contact.data)
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
        db.session.add(user)
        db.session.commit()
        print("validated")
        print("validated")
        flash('You were successfully signed up')
        return redirect(url_for('index'))
           
    return render_template('cateror.html', title='catRegister', form=form)

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    organizer = User.query.filter_by(id=current_user.id).first()
    print(organizer)
    if form.validate_on_submit():

        organizer = User(name = form.name.data, email=form.email.data)

        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            organizer.image_file = picture_file
            print('profile picture updated')

        db.session.commit()
        flash('Your account has been updated!')
        return redirect(url_for('account'))

    elif request.method == 'GET':
        form.name.data = organizer.name
        form.email.data = organizer.email

    image_file = url_for('static', filename='profile_pics/' + organizer.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form, organizer=organizer)