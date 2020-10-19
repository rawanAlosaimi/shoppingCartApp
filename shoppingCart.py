import sales.shopping_Cart, sales.shopping_Order


cart = sales.shopping_Cart.Cart()

order = sales.shopping_Order.Order()

order.get_input()

while not order.quit:

    cart.process(order)

    order = sales.shopping_Order.Order()
    order.get_input()


print(cart)


