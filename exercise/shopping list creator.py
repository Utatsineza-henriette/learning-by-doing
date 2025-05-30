shopping_list = []
item1 = input('enter item 1 : ')
item2 = input('enter item 2 : ')
item3 = input('enter item 3 : ')
shopping_list.append(item1)
shopping_list.append(item2)
shopping_list.append(item3)
print(f'your shopping list is:')
for item in shopping_list:
    print(f"-{item}")
