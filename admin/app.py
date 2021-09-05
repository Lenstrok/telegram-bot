from flask import Flask
from flask_admin import Admin, AdminIndexView

from db import current_session
from db.individ import Individual, TaxableIncome, Agent

app = Flask(__name__)


def create_app() -> Flask:
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.secret_key = 'kek'

    admin = Admin(app, name='Админка', index_view=AdminIndexView(name='lol', url='/'), template_mode='bootstrap4')

    from admin_original.views.agent import AgentView
    from admin_original.views.income import IncomeView
    from admin_original.views.individual import IndividualView

    admin.add_view(IndividualView(Individual, current_session, name='Физлицо'))
    admin.add_view(AgentView(Agent, current_session, name='Агент'))
    admin.add_view(IncomeView(TaxableIncome, current_session, name='Доход'))

    return admin.app


if __name__ == '__main__':
    from db import DBSettings

    DBSettings().setup_db()

    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
