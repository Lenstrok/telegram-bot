from flask_admin.contrib.sqla import ModelView
from flask_admin.model.form import InlineFormAdmin


class IncomeView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ['individual', 'month', 'sum']

    column_sortable_list = ['created_at', 'month']


class IncomeInlineAdmin(InlineFormAdmin):
    form_excluded_columns = ['individual', 'individual_id', 'created_at']
