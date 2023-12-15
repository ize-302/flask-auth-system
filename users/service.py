from flask import jsonify
from app import db
from users.models import UsersModel

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import current_user
from flask_jwt_extended import get_jwt_identity

# login service
def login_service(request, input_data):
  """
  check if email exists
  check if password is correct
  create user session
  """
  found_user = UsersModel.query.filter_by(email_address=input_data.get('email_address')).first()
  password_is_correct = UsersModel.check_password(found_user, input_data.get('password'))
  
  if input_data.get('email_address') == "" or input_data.get('password') == "":
     return jsonify({"error": "Email and password required"}), 401
  if found_user is None or not password_is_correct:
    return jsonify({"error": "Incorrect login details. Try again"}), 401
  if password_is_correct:
    # generate token or session here ->
    access_token = create_access_token(identity=found_user.id, fresh=True)
    refresh_token = create_refresh_token(identity=found_user.id)
    return jsonify(refresh_token=refresh_token, access_token=access_token), 200


# register service
def register_service(request, input_data):
  """
  check if email already exists
  create new user if email doesn't exist
  """
  found_user = UsersModel.query.filter_by(email_address=input_data.get('email_address')).first()
  if found_user:
    return jsonify({"error": "Email already registered. Try another email address"}), 409
  else:
    new_user = UsersModel(**input_data)
    UsersModel.hash_password(new_user)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Account created"}), 201
  

def change_password_service(request, input_data):
  """change current user's password
  validate if current password is correct
  update to new provided password if current password is correct
  """
  current_password = input_data.get('current_password')
  new_password = input_data.get('new_password')
  current_user = get_jwt_identity()

  found_user = UsersModel.query.filter_by(id=current_user).first()
  current_password_is_correct = UsersModel.check_password(found_user, current_password)
  
  if current_password == "" or new_password == "":
    return jsonify({"error": "Password fields are required. Try again"}), 401
  
  if current_password_is_correct == False:
    return jsonify({"error": "Incorrect password. Try again"}), 401
  else:
    found_user.password = new_password
    UsersModel.hash_password(found_user)
    db.session.commit()
    return jsonify({"message": "Password changed"}), 201

def user_profile_service(request, id):
  found_user = UsersModel.query.filter_by(id=id).first()
  data = {
    "id": found_user.id,
    "email_address": found_user.email_address,
    "full_name": found_user.full_name,
    "created_at": found_user.created_at
  }
  return data, 200