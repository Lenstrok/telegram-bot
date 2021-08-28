from flask_admin.contrib.sqla import ModelView
from flask_admin.model.form import InlineFormAdmin


class AgentView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ['individual', 'phone', 'inn', 'kpp', 'agent_name']

    column_sortable_list = ['created_at']


class AgentInlineAdmin(InlineFormAdmin):
    form_excluded_columns = ['individual', 'individual_id', 'created_at']
