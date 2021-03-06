from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from py.models import Base

db = SQLAlchemy(model_class=Base)


def init_db(app):
    db.init_app(app)
    migrate = Migrate(app, db)

    # modelとして定義した全テーブルをCreateする
    db.create_all(app=app)
