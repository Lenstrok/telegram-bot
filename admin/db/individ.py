import sqlalchemy as sa
import sqlalchemy.orm as so

from admin_original.db import BaseTable


class Individual(BaseTable):

    name = sa.Column(sa.Text, nullable=False, doc='Имя')
    family_name = sa.Column(sa.Text, nullable=False, doc='Фамилия')
    forname = sa.Column(sa.Text, nullable=False, doc='Отчество')
    birth_date = sa.Column(sa.Date, nullable=False, doc='Дата рождения')
    inn = sa.Column(sa.Integer, nullable=False, unique=True, doc='ИНН в РФ')


class Agent(BaseTable):

    agent_name = sa.Column(sa.Text, nullable=False, doc='Налоговый агент')
    phone = sa.Column(sa.Integer, nullable=False, doc='Номер телефона')
    inn = sa.Column(sa.Integer, nullable=False, unique=True, doc='ИНН')
    kpp = sa.Column(sa.Integer, nullable=False, unique=True, doc='КПП')


class TaxableIncome(BaseTable):

    month = sa.Column(sa.Integer, nullable=False, doc='Месяц')
    sum = sa.Column(sa.Integer, nullable=False, doc='Сумма дохода')
