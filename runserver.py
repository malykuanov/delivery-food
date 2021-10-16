from app import create_app, db
from app.home.views import home
from app.admin.views import admin, create_admin, CategoryView, ProductView, UsersView
from app.products.models import Product, ProductCategory
from app.auth.models import Users
from app.products.views import products

from config import DevelopmentConfig


app = create_app(DevelopmentConfig)
app.register_blueprint(home)
app.register_blueprint(admin)
app.register_blueprint(products)

admin = create_admin(app)
admin.add_view(ProductView(Product, db.session))
admin.add_view(CategoryView(ProductCategory, db.session))
admin.add_view(UsersView(Users, db.session))

if __name__ == '__main__':
    app.run()
