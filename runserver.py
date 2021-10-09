from app import create_app, db
from app.home.views import home

app = create_app()
app.register_blueprint(home)

if __name__ == '__main__':
    app.run()
