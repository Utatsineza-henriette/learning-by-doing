cart = []
while True:
    item_name = input('enter the item name:')
    if item_name == 'done':
        break
    cart.append(item_name)
    print('\nshopping cart: ')
    for items in cart:
        print(items)