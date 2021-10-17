from flask import Blueprint

from app.auth.models import Users


auth = Blueprint('auth', __name__)
