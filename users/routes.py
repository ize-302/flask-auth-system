from flask_restful import Api
from users.views import IndexApi, LoginApi, RegisterApi, ChangePasswordApi, ResetPasswordApi, ForgotPasswordApi, UserProfileApi

def create_authentication_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    """
    
    api.add_resource(IndexApi, "/")
    # auth
    api.add_resource(LoginApi, "/login")
    api.add_resource(RegisterApi, "/register")
    api.add_resource(ChangePasswordApi, "/change-password")
    # user
    api.add_resource(UserProfileApi, "/user/<id>/")