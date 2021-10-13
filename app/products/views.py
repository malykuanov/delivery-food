from flask import Blueprint, render_template, url_for, abort

from app.products.models import ProductCategory

products = Blueprint(
    'products',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/home-static'
)


@products.route("/<product_category>", methods=['GET'])
def index(product_category):
    category = ProductCategory.query.order_by(ProductCategory.id).all()
    category_name = [category[i].category for i in range(0, len(category))]
    if product_category not in category_name:
        abort(404)
    return render_template('products/products.html', product_category=product_category, category=category)
