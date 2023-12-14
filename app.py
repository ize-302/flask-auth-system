from flask import Flask, request, jsonify, request
import os
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)
# db  connect
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ozorku:postgres@localhost:5432/flask_auth_system_db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# models
class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String())
    email_address = db.Column(db.String())
    password = db.Column(db.String())
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow())

    def __init__(self, full_name, email_address, password):
        self.full_name = full_name
        self.email_address = email_address
        self.password = password

    def __repr__(self):
        return f"<User {self.email_address} {self.full_name} {self.password} {self.created_at}>"

# routes
@app.route("/")
def index():
  return jsonify({"message": "hello world"}), 200

# register
@app.route("/auth/register", methods=['POST'])
def register():
  post_data = request.get_json()
  # check if email already exists
  found_user = UsersModel.query.filter_by(email_address=post_data.get('email_address')).all()
  if len(found_user) > 0:
    return jsonify({"error": "Email already registered. Try another email address"}), 409
  # continue
  hashed_password = bcrypt.generate_password_hash(post_data.get('password')).decode('utf-8')
  data = {
    "email_address": post_data.get('email_address'),
    "full_name": post_data.get('full_name'),
    "password": hashed_password
  }  
  new_user = UsersModel(full_name=data['full_name'], email_address=data['email_address'], password=data['password'])
  db.session.add(new_user)
  db.session.commit()
  return jsonify({"message": "Account created"}), 201

# login
@app.route("/auth/login", methods=['POST'])
def login():
  post_data = request.get_json()
  found_user = UsersModel.query.filter_by(email_address=post_data.get('email_address')).all()

  is_valid_password = bcrypt.check_password_hash(found_user[0].password, post_data.get('password')) if len(found_user) > 0 else []
  
  if len(found_user) == 0 or not is_valid_password:
    return jsonify({"error": "Incorrect login details. Try again"}), 401
  
  return jsonify({"message": "Log in successful"}), 201
  
if __name__ == '__main__':
    app.run(debug=True)