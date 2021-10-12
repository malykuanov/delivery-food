from flask import Blueprint, render_template, url_for

from app.products.models import ProductCategory


home = Blueprint(
    'home',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/home-static'
)


@home.route("/")
def index():
    category = ProductCategory.query.order_by(ProductCategory.id).all()
    return render_template('home/home.html', category=category)
