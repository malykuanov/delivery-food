from flask import Blueprint, url_for, request
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_login import current_user
from werkzeug.utils import redirect

from app import db
from app.products.models import Product, ProductCategory
admin = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')


def create_admin(app):
    admin = Admin(app, name='Delivery_food_AP', template_mode='bootstrap3')
    return admin
