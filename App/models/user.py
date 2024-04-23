from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
#from .applications import Applications

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False, default='student')
    applications = db.relationship('Applications', backref='user', lazy=True, cascade='all, delete-orphan')
    interships = db.relationship('Internships', backref='user', lazy=True, cascade='all, delete-orphan')

    def __init__(self, username, password, role='student'):
        self.username = username
        self.set_password(password)
        self.role = role

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

