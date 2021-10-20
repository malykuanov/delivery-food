from flask import Blueprint

cart = Blueprint(
    'CartProducts',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/home-static'
)
