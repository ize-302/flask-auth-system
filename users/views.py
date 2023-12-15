from flask import Response, request, make_response
from flask_restful import Resource
from users.service import login_service, register_service, change_password_service, user_profile_service
from flask_jwt_extended import jwt_required

class IndexApi(Resource):
  @staticmethod
  def get() -> Response:
    return 'hello'

class LoginApi(Resource):
  @staticmethod
  def post() -> Response:
    input_data = request.get_json()
    response, status = login_service(request, input_data)
    return make_response(response, status)
      
class RegisterApi(Resource):
  @staticmethod
  def post() -> Response:
    input_data = request.get_json()
    response, status = register_service(request, input_data)
    return make_response(response, status)
      
class ChangePasswordApi(Resource):
  @staticmethod
  @jwt_required()
  def post() -> Response:
    input_data = request.get_json()
    response, status = change_password_service(request, input_data)
    return make_response(response, status)
    
class UserProfileApi(Resource):
  @staticmethod
  @jwt_required()
  def get(id) -> Response:
    response, status = user_profile_service(request, id)
    return make_response(response, status)
       