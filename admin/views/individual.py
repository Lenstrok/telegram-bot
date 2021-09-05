from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ['id', 'full_name', 'phone_number']

    column_sortable_list = ['id']

    edit_template = 'individual_edit.html'


#
# class IndividualView(ModelView):
#     can_edit = True
#     can_create = True
#     can_delete = True
#     can_view_details = True
#
#     form_columns = ['name', 'family_name', 'forname', 'birth_date', 'inn']
#
#     column_sortable_list = ['created_at']
#
#     edit_template = 'individual_edit.html'
#
