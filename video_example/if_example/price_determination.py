price = 1000000
has_good_credit = False
if has_good_credit:
    print('they need to putdown 10% ')
    new_price = price*10/100
else:
    print(f'they need to putdown 20% ')
    new_price = price*20/100
print(f'the down payment is : {new_price}')    
