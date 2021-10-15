import os

from flask import Blueprint, current_app
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_wtf.file import FileField, FileAllowed, FileSize, FileRequired
from werkzeug.utils import secure_filename
from slugify import slugify

admin = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')


class CategoryView(sqla.ModelView):
    form_excluded_columns = ('photo_url', 'products')
    form_extra_fields = {
        'category_photo': FileField(validators=[
            FileAllowed(['png', 'jpg', 'jpeg'], "Wrong format! only png, jpg"),
            FileSize(max_size=5 * (10 ** 6), message="Max size = 5 Mb")
        ])
    }

    def set_category_image(self, form, model):
        storage_file = form.category_photo.data
        if storage_file:
            filename = secure_filename(storage_file.filename)
            filename = slugify(form.category.data) + '_category_photo.' + filename.rsplit('.', 1)[1]
            path = current_app.root_path + '/static/images/product_category/' + filename
            os.remove(path) if os.path.exists(path) else None
            storage_file.save(path)
            return filename
        return model.photo_url


    def _on_model_change(self, form, model, is_created):
        model.photo_url = self.set_category_image(form, model)
        return super(CategoryView, self).on_model_change(form, model, is_created)


class ProductView(sqla.ModelView):
    form_excluded_columns = ('photo_url')
    form_extra_fields = {
        'product_photo': FileField(validators=[
            FileAllowed(['png', 'jpg', 'jpeg'], "Wrong format! only png, jpg"),
            FileSize(max_size=10 * (10 ** 6), message="Max size = 10 Mb"),
        ])
    }

    def set_product_image(self, form, model):
        storage_file = form.product_photo.data
        if storage_file:
            filename = secure_filename(storage_file.filename)
            filename = slugify(form.name.data) + '_photo.' + filename.rsplit('.', 1)[1]
            path = current_app.root_path + f'/static/images/products/{slugify(str(form.product_category.data))}/'
            if not os.path.exists(path):
                os.makedirs(path)
            path += filename
            os.remove(path) if os.path.exists(path) else None
            storage_file.save(path)
            return filename
        else:
            return model.photo_url

    def _on_model_change(self, form, model, is_created):
        model.photo_url = self.set_product_image(form, model)
        return super(ProductView, self).on_model_change(form, model, is_created)


def create_admin(app):
    admin = Admin(app, name='Delivery_food_AP', template_mode='bootstrap3')
    return admin
