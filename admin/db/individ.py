import sqlalchemy as sa

from admin.db import BaseTable


# class Individual(BaseTable):
#
#     name = sa.Column(sa.Text, nullable=False, doc='Имя')
#     family_name = sa.Column(sa.Text, nullable=False, doc='Фамилия')
#     forname = sa.Column(sa.Text, nullable=False, doc='Отчество')
#     birth_date = sa.Column(sa.Date, nullable=False, doc='Дата рождения')
#     inn = sa.Column(sa.Integer, nullable=False, unique=True, doc='ИНН в РФ')
