from flask import Blueprint, render_template, abort

from app.products.models import ProductCategory, Product

products = Blueprint(
    'products',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/home-static'
)


@products.route("/<product_category>", methods=['GET'])
def index(product_category):
    categories = ProductCategory.query.all()
    if product_category not in [category.slug for category in categories]:
        abort(404)
    products = Product.query.all()
    products_for_category = [product for product in products if product.product_category.slug == product_category]
    return render_template('products/products.html',
                           categories=categories,
                           products=products_for_category,
                           product_category=product_category)
