from flask import Blueprint, render_template, abort
from slugify import slugify

from app.products.models import ProductCategory, Product

products = Blueprint(
    'products',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/home-static'
)


@products.route("/<product_category>", methods=['GET'])
def category(product_category):
    categories = ProductCategory.query.all()
    if product_category not in [category.slug for category in categories]:
        abort(404)
    products = Product.query.all()
    products_for_category = [product for product in products if product.product_category.slug == product_category]
    return render_template('products/category.html',
                           categories=categories,
                           products=products_for_category,
                           product_category=product_category)


@products.route("/<product_category>/<product>", methods=['GET'])
def category_product(product_category, product):
    categories = ProductCategory.query.all()
    if product_category not in [category.slug for category in categories]:
        abort(404)
    products = Product.query.filter(Product.product_category.has(slug=product_category)).all()
    if product not in [slugify(pr.name) for pr in products]:
        abort(404)
    return render_template('products/product.html',
                           categories=categories,
                           product_category=product_category)
