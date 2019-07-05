from init import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    occasion = db.Column(db.String(120))
    location = db.Column(db.String(120)) 
    price = db.Column(db.Integer)
    address = db.Column(db.String(120))
    contact = db.Column(db.Integer, unique=True)
    requirement=db.Column(db.String(80))
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
   
    

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.occasion}', '{self.location}', '{self.price}', '{self.address}', '{self.contact}', '{self.requirement}')"
   
def __init__(self,name,email):
   self.name = name
   self.email=email
   self.location=location
   self.price=price
   self.contact=contact

