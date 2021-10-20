from flask import Blueprint, render_template, abort

from app.auth.models import get_price_and_count
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
    if product_category not in [category.slug for category in ProductCategory.get_all_categories()]:
        abort(404)
    products = Product.query.all()
    products_for_category = [product for product in products if product.product_category.slug == product_category]
    return render_template('products/category.html',
                           categories=ProductCategory.get_all_categories(),
                           products=products_for_category,
                           product_category=product_category,
                           price=get_price_and_count()['price'],
                           count=get_price_and_count()['count'])


@products.route("/<product_category>/<product>", methods=['GET'])
def category_product(product_category, product):
    if product_category not in [category.slug for category in ProductCategory.get_all_categories()]:
        abort(404)
    products = Product.query.filter(Product.product_category.has(slug=product_category)).all()
    if product not in [product.slug for product in products]:
        abort(404)
    product = Product.query.filter_by(slug=product).first()
    return render_template('products/product.html',
                           categories=ProductCategory.get_all_categories(),
                           product_category=product_category,
                           product=product,
                           price=get_price_and_count()['price'],
                           count=get_price_and_count()['count'])
