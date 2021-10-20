from flask import Blueprint, render_template
from flask_login import current_user
from slugify import slugify

from app.auth.models import Users, get_price_and_count
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
    categories = ProductCategory.query.order_by(ProductCategory.id).all()
    return render_template('home/home.html',
                           categories=categories,
                           price=get_price_and_count()['price'],
                           count=get_price_and_count()['count'])

