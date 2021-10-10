from app import create_app, db
from app.home.views import home
from app.products.models import Product, ProductCategory

from config import DevelopmentConfig


app = create_app(DevelopmentConfig)
app.register_blueprint(home)

if __name__ == '__main__':
    app.run()
