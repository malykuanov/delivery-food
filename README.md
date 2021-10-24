# Flask application: "Delivery food"

|   Directory   | Description                                                                                                                                                                                              |
|:-------------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   app/admin/  | Admin panel for managing models, access only for users with the admin role                                                                                                                               |
|    app/api/   | API for the service, Flask-restx is used. Example GET, POST, PUT, DELETE for Product model. /api/doc/ displays Swagger UI interface                                                                                                               |
|   app/auth/   | Module for login, registration and logout of users. Contains User and СartProduct models                                                                                                                 |
|   app/home/   | Home page with navigation by product categories and site structure (navbar, sliders, body, footer ...)                                                                                                   |
| app/products/ | Module with Product and ProductCategory models. Views contain a list of products for a specific category and  detailed information about each product (name, description, composition, weight and price) |
|   app/users/  | The module contains a view representing a specific user's product cart (which products are selected and the total cost)                                                                                  |
|   migrations  | Migrations for DB (Flask-Migrate)

```
app/                 Application directory with modules
migrations/          Migrations for DB (Flask-Migrate)
README               this file
config               Project configuration file(Production, Development, Testing)
requirements         “Requirements files” are files containing a 
                     list of items to be installed using pip install
runserver            Application Launch File (create application, register blueprints, 
                     create Admin Panel and register model`s views in Admin Panel)
```

### Contacts for communication

* 8-916-191-51-85
* malykuanov@mail.ru
* @white_bunny_hop (TG)