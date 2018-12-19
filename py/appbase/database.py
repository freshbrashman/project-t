from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    migrate = Migrate(app, db)

    # modelとして定義した全テーブルをCreateする
    db.create_all(app=app)
