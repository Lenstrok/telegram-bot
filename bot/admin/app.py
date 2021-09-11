from flask import Flask
from flask_admin import Admin, AdminIndexView

# from db import current_session
from bot.database import User

app = Flask(__name__)


def create_app() -> Flask:
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.secret_key = 'kek'

    admin = Admin(app, name='Админка', index_view=AdminIndexView(name='lol', url='/'), template_mode='bootstrap4')

    from bot.admin.views.individual import UserView

    from bot.database.engine import engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    current_session = scoped_session(sessionmaker(bind=engine))

    # with Session() as session:
    admin.add_view(UserView(User, current_session, name='Пользователь'))

    return admin.app


if __name__ == '__main__':
    # from db import DBSettings
    #
    # DBSettings().setup_db()

    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
