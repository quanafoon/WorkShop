from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
#from .applications import Applications

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    firstName = db.Column(db.String(120))
    lastName = db.Column(db.String(120))
    pic = db.Column(db.String(120))
    

    def __init__(self, username, password, firstName, lastName, pic):
        self.username = username
        self.set_password(password)
        self.firstName = firstName
        self.lastName = lastName
        self.pic = pic

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'role': self.role
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

