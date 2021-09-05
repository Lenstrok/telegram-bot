from flask_admin.contrib.sqla import ModelView

from admin_original.views.agent import AgentInlineAdmin
from admin_original.views.income import IncomeInlineAdmin
from admin_original.db import Agent, TaxableIncome


class IndividualView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ['name', 'family_name', 'forname', 'birth_date', 'inn']

    column_sortable_list = ['created_at']

    edit_template = 'individual_edit.html'

    inline_models = (AgentInlineAdmin(Agent), IncomeInlineAdmin(TaxableIncome))
