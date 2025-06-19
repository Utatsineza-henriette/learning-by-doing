orders = []
num_drink = int(input('how many drinks ordered: '))
for _ in range(num_drink):
    drink = input('enter the name of the drink:')
    orders.append(drink)
print('list of drinks ordered: ')
for drink in orders:
    print(drink)


      