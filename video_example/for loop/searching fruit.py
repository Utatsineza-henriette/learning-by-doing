basket = []
num_fruits = int(input('how many fruits you want to add to a basket?: '))
for _ in range(num_fruits):
    name = input('friuts name: ')
    basket.append(name)
print('lists of fruits: ')

for fruit in basket:
    print(fruit)
 
search = input('fruit to be searched: ')

if search in basket:
    print(f'{search} is in the basket')
else:
    print(f'{search} is not in the basket')
