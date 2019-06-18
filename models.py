from init import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    spaceused = db.Column(db.String(120))
    Location = db.Column(db.String(120)) 
    price = db.Column(db.Integer, unique=True, nullable=False)
    address = db.Column(db.String(120))
    contact = db.Column(db.Integer, unique=True, nullable=False)
    details = db.Column(db.String(120), unique=True, nullable=False)
    knownfor = db.Column(db.String(120))
    

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.spaceused}', '{self.Location}', '{self.price}', '{self.address}', '{self.contact}', '{self.details}', '{self.knownfor}')"


