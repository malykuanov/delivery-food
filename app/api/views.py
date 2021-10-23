from flask import Blueprint, jsonify
from flask_restx import Api, Resource

from app.products.models import Product, ProductSchema

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp,
          version='1.0',
          title='Delivery_food API',
          description='API for the "Delivery_food" service',
          doc='/doc/')


@api.route('/product')
class Products(Resource):
    """Get all products"""

    def get(self):
        query = Product.query.all()
        product_schema = ProductSchema(many=True)
        result = product_schema.dump(query)
        return jsonify(result)

