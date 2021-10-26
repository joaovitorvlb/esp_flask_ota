from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql://admin:root@localhost/device_manager"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["UPLOAD_FOLDER"] = os.path.dirname(os.path.abspath(__file__)) + "/bin"
    app.config["SECRET_KEY"] = "Kri57i4n570bb33r3nF1ink3rFyr"
    db.init_app(app)
    migrate.init_app(app, db)
    from app import assinatura

    assinatura.init_app(app)

    return app
