from datetime import datetime
from app import db
from flask_login import UserMixin


class Product(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(500))
    category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    price = db.Column(db.Numeric(5, 2))

    def __str__(self):
        return f"id={self.id}, name={self.name}, price={self.price}"


class ProductCategory(db.Model):
    __tablename__ = 'product_category'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), unique=True, nullable=False)

    product = db.relationship('Product', backref='product_category', uselist=False)

    def __str__(self):
        return f"id={self.id}, category={self.category}"
