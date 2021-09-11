from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ['id', 'full_name', 'phone_number']

    column_sortable_list = ['id']

    page_size = 25
    edit_template = 'individual_edit.html'

    column_labels = {
        'id': 'Идентификатор',
        'full_name': 'ФИО',
        'phone_number': 'Номер телефона',
    }
