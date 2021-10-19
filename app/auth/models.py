from datetime import datetime

from flask_login import UserMixin

from app import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), default="User")
    address = db.Column(db.String(500))
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500))
    role = db.Column(db.String(50), default='user')
    date_registration = db.Column(db.DateTime, default=datetime.utcnow)

    cart = db.relationship('Cart', backref='users', uselist=False)

    def has_role(self, role):
        return role == self.role

    def __str__(self):
        return f"{self.email}"


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    cart_products = db.relationship('CartProduct',
                                    foreign_keys='CartProduct.cart_id',
                                    backref='cart',
                                    lazy='dynamic',
                                    cascade='all, delete-orphan')


assoc_cart_products = db.Table("assoc_cart_products",
                               db.Column("cart_product_id", db.Integer, db.ForeignKey("cart_product.id")),
                               db.Column("product_id", db.Integer, db.ForeignKey("product.id")))


class CartProduct(db.Model):
    __tablename__ = 'cart_product'
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    products = db.relationship("Product", backref="cart_product", secondary=assoc_cart_products)


def get_user(user_id):
    res = Users.query.get(user_id)
    if not res:
        return False
    else:
        return res
