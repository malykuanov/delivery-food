from flask import Blueprint
from flask_restx import Api


api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp,
          version='1.0',
          title='Delivery_food API',
          description='API for the "Delivery_food" service',
          doc='/doc/')

