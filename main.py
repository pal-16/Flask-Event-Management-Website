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

from forms import RegistrationForm,cRegistrationForm,dRegistrationForm,LoginForm,uRegistrationForm,UpdateAccountForm,planRegistrationForm,dynamicForm
from models import Org,User,Plan
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

@app.route("/detail/<int:org_id>")
def org(org_id):
    org = Org.query.get_or_404(org_id)
    return render_template('fd.html', title='full details', org=org)



@app.route("/display")
def display():
    return render_template('detail.html')





@app.route("/partyhosts")
def partyhosts():
    return render_template('partyhosts.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")  
def contact():
    return render_template('contact.html')

@app.route('/afterreg')
def afterreg():
   return render_template('afterreg.html')


@app.route('/flas')
def flas():
   return render_template('flas.html')

@app.route("/find_test/<org_price>")
def find_test(org_price):
   org_price= sorted(org_price, key=lambda org: org_price) 
   print(org_price)
   return render_template('reverse.html',title='match',org_price=org_price)
  
@app.route("/find_test1")
def find_test1():
    sorted_list=[]
    for org in org :
        print(org.price)
        sorted_list.append(org.price)
    
    print(sorted_list)
    print("success 2")
    print("validated")
    return render_template('test.html',title='match',sorted_list=sorted_list)

   
@app.route('/find',methods=['GET', 'POST'])
def find():
    form = uRegistrationForm()
    if form.location.data:    
        print(form.requirement.data+" "+form.location.data)
        orgList= Org.query.filter_by(location=form.location.data,requirement=form.requirement.data).all()
        print("happening")
        print(orgList)
    else :
        orgList= Org.query.filter_by(requirement=form.requirement.data).all()
                
    return render_template('detail.html', title='Find', orgList=orgList, form=form)

 
@app.route('/findd',methods=['GET', 'POST'])
def findd():
    form = dynamicForm()
    if form.location.data:    
       org= Org.query.filter_by(location=form.location.data,price=form.price.data).all()
    else :
        org= Org.query.filter_by(price=form.requirement.data).all()
    if org:                     
                              print("success2")
                              user = User.query.filter_by(id=current_user.id).first()
                              user.location = form.location.data
                              user.price = form.price.data
                              db.session.commit()
                      
                              print("User")
                              print(user)
                      
                              print('in filter')
    return render_template('detail.html', title='Find', org=org, form=form)
  
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        org =Org.query.filter_by(email=form.email.data).first()
        print("good")
        if org and bcrypt.check_password_hash(org.password, form.password.data):
            print("palak")
            login_user(org, remember=form.remember.data)

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

@app.route("/hd")
def hd():
    org = Org.query.all()
    return render_template('flashhall.html', org=org)

@app.route("/decd")
def decd():

    org = Org.query.filter_by(requirement='decorators').all()           #problem ask***
    return render_template('flashdec.html', org=org)

@app.route("/catd")
def catd():
    org = Org.query.all()
    return render_template('flashhall.html', org=org)

@app.route("/pd")
def pd():
    plan = Plan.query.all()
    return render_template('flashparty.html', plan=plan)

@app.route("/register", methods=['GET', 'POST'])
def register():
    
    return render_template('typereg.html')

@app.route("/partyplan", methods=['GET', 'POST'])
def partyplan():
    form = planRegistrationForm() 
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            
        plan = Plan(name=form.name.data,email=form.email.data,password=hashed_password,special=form.special.data)

        
        db.session.add(plan)
        db.session.commit()
        print("Org")
        print(plan)
        print("validated")
        flash('You were successfully signed up')
        return redirect(url_for('afterreg'))
    return render_template('partyplan.html',title='party',form=form)


@app.route("/hregister", methods=['GET', 'POST'])
def hallreg():                                   
    form = RegistrationForm()
     # flow of control is from top to bottom; so the logic TO BE PASSED to temp.html is written first, SO THAT it can be passed  okay thanks
    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            
        org = Org(name=form.name.data,email=form.email.data,password=hashed_password,location=form.location.data,price=form.price.data,contact=form.contact.data,address=form.address.data,requirement='h')

        
        db.session.add(org)
        db.session.commit()
        print("Org")
        print(org)
        print("validated")
        flash('You were successfully signed up')
        return redirect(url_for('afterreg'))

    
    return render_template('hall.html', title='Register',form=form)
      
@app.route("/decreg", methods=['GET', 'POST'])
def decreg():
    form = dRegistrationForm()
    if form.validate_on_submit():
        
        org = Org(name = form.name.data,email=form.email.data,password=form.password.data,requirement=form.requirement.data,price=form.price.data,contact=form.contact.data)
        db.session.add(org)
        db.session.commit()
        print("validated")
        print(Org)
        flash('You were successfully signed up')
        return redirect(url_for('afterreg'))
        
    return render_template('dec.html', title='decregister', form=form)

@app.route("/catererreg", methods=['GET', 'POST'])
def catererreg():
    form = cRegistrationForm()
    print("hi palak going well")
    if form.validate_on_submit():
        print("validated")
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        org = Org(name=form.name.data,email=form.email.data,password=form.password.data,requirement=form.requirement.data,price=form.price.data,contact=form.contact.data)
        db.session.add(org)
        db.session.commit()
        print("validated")
       
        flash('You were successfully signed up')
        return redirect(url_for('afterreg'))
           
    return render_template('caterer.html', title='catRegister', form=form)

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():

        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.name = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)

