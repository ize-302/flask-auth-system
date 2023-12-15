import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from app import db
from flask_login import (
  UserMixin,
)
from datetime import datetime

class UsersModel(UserMixin, db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  full_name = db.Column(db.String(), nullable=False,)
  email_address = db.Column(db.String(), nullable=False,)
  password = db.Column(db.String(), nullable=False,)
  created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow())

  def __init__(self, **kwargs):
    self.full_name = kwargs.get('full_name')
    self.email_address = kwargs.get('email_address')
    self.password = kwargs.get('password')

  def __repr__(self):
    return f"<User {self.id} {self.email_address} {self.full_name} {self.password} {self.created_at}>"

  def hash_password(self):
    """
    It takes the password that the user has entered, hashes it, and then stores the hashed password in
    the database
    """
    self.password = generate_password_hash(self.password).decode("utf8")

  def check_password(self, password):
    """
    It takes a plaintext password, hashes it, and compares it to the hashed password in the database
    
    :param password: The password to be hashed
    :return: The password is being returned.
    """
    return check_password_hash(self.password, password)