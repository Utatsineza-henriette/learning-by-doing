pack = []
num_gifts = int(input('how many gifts you want to pack: '))

for _ in range(num_gifts):
    name_gifts = input('the name of the gift: ')
    pack.append(name_gifts)
print('\nlist of the gift:') 

for gift in pack:
    print(f'packing {gift}...')