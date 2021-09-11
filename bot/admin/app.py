from flask import Flask
from flask_babelex import Babel
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import sessionmaker, scoped_session

from bot.database import User, Product
from bot.admin.views import UserView
from bot.database.engine import engine

app = Flask(__name__)


def create_app() -> Flask:
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
    app.secret_key = 'kek'

    babel = Babel(app)
    admin = Admin(
        app=babel.app,
        name='Управление ботом',
        index_view=AdminIndexView(name='lol', url='/admin'),
        template_mode='bootstrap4'
    )

    current_session = scoped_session(sessionmaker(bind=engine))

    admin.add_view(UserView(User, current_session, name='Пользователь'))
    admin.add_view(ModelView(Product, current_session, name='Товар'))

    return admin.app


if __name__ == '__main__':  # todo rm ->

    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
