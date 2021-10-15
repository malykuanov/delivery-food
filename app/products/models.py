from slugify import slugify

from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(500))
    composition = db.Column(db.String(500))
    weight = db.Column(db.Integer)
    price = db.Column(db.Numeric(5, 0))
    photo_url = db.Column(db.String(100))

    category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))

    def __str__(self):
        return f"id={self.id}, name={self.name}, price={self.price}"


class ProductCategory(db.Model):
    __tablename__ = 'product_category'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), unique=True, nullable=False)
    photo_url = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True, nullable=False)

    products = db.relationship('Product',
                               foreign_keys='Product.category_id',
                               backref='product_category',
                               lazy='dynamic',
                               cascade='all, delete-orphan')

    def generate_slug(self):
        if self.category:
            self.slug = slugify(self.category)

    def __str__(self):
        return f"{self.category}"
