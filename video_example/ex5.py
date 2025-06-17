price = 1000000
is_good_credit = False
if is_good_credit:
    print('they need to putdown 10% ')
    new_price = price*10/100
else:
    print(f'they need to putdown 20% ')
    new_price = price*20/100
print(f'the down payment is : {new_price}')    
