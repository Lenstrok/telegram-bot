from bot.database.models import User, Order, OrderedProduct, Product
from bot.database.crud import users, orders, ordered_products, products
from bot.database.engine import Session


# if __name__ == '__main__':  # todo rm ->
#
#     with Session() as session:
#
#         # create user
#         # user_id = users.create(session, 7)
#
#         # add
#         # product = products.get_by_name(session, "book")
#         #
#         # orders.add(session, 7, product.id)
#         #
#         # session.commit()
#
#         # remove
#         # product = products.get_by_name(session, "book")
#         #
#         # orders.remove(session, 7, product.id)
#         #
#         # session.commit()
#
#         # get_order
#         order = orders.get_by_user_id(session, user_id=7)
#         print(order.__dict__)
#         print(order.ordered_product[0].__dict__)
