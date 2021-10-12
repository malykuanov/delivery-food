import os

from flask import Blueprint, current_app, request, flash
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_wtf.file import FileField, FileAllowed, FileSize, FileRequired
from werkzeug.utils import secure_filename

from app import db
from app.products.models import ProductCategory

admin = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')


class ProductCategoryAdminModel(sqla.ModelView):
    form_excluded_columns = ('photo_url', 'product')
    form_extra_fields = {
        'category_photo': FileField(validators=[
            FileAllowed(['png', 'jpg', 'jpeg'], "Wrong format! only png, jpg"),
            FileSize(max_size=5 * (10 ** 6), message="Max size = 5 Mb"),
            FileRequired()
        ])
    }

    def set_category_image(self, _form):
        try:
            storage_file = _form.category_photo.data
            filename = secure_filename(storage_file.filename)
            if storage_file and filename.rsplit('.', 1)[1] in ['png', 'jpg', 'jpeg']:
                if request.args.get('id', type=int):
                    category = ProductCategory.query.get(request.args.get('id', type=int))
                else:
                    category = ProductCategory(category=list(_form)[0].data)
                    db.session.add(category)
                    db.session.flush()
                filename = category.category + '_category_photo.' + filename.rsplit('.', 1)[1]
                path = current_app.root_path + '/static/images/product_category/' + filename
                os.remove(path) if os.path.exists(path) else None
                storage_file.save(os.path.join(path))
                category.photo_url = filename
                db.session.commit()
        except Exception as ex:
            print(ex)

        return _form

    def edit_form(self, obj=None):
        return self.set_category_image(
            super(ProductCategoryAdminModel, self).edit_form(obj)
        )

    def create_form(self, obj=None):
        flash(message='"Already exists" on "Save" means the record was successfully added')
        return self.set_category_image(
            super(ProductCategoryAdminModel, self).create_form(obj)
        )


def create_admin(app):
    admin = Admin(app, name='Delivery_food_AP', template_mode='bootstrap3')
    return admin
