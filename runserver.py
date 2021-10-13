from flask_admin.contrib.sqla import ModelView

from app import create_app, db
from app.home.views import home
from app.admin.views import admin, create_admin, ProductCategoryAdminModel
from app.products.models import Product, ProductCategory
from app.products.views import products

from config import DevelopmentConfig


app = create_app(DevelopmentConfig)
app.register_blueprint(home)
app.register_blueprint(admin)
app.register_blueprint(products)

admin = create_admin(app)
admin.add_view(ModelView(Product, db.session, category="Products"))
admin.add_view(ProductCategoryAdminModel(ProductCategory, db.session, category="Products"))

if __name__ == '__main__':
    app.run()
