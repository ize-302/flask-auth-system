"""App entry point."""
"""Initialize Flask app."""
import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
  """Construct the core application."""
  app = Flask(__name__, instance_relative_config=False)
  
  app.config.from_object("config.Config")  # load config settings
  
  JWTManager(app)

  api = Api(app=app)

  from users.routes import create_authentication_routes

  create_authentication_routes(api=api)

  db.init_app(app)

  with app.app_context():

    db.create_all()  # Create database tables for our data models

    return app
  
if __name__ == "__main__":
  app = create_app()