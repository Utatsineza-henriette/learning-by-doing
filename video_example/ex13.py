balance = 0
while True:
    action = input('choose the action(check, deposit, withdraw, exit): ')
    
    if action == 'check':
        print(balance)

    elif action == 'deposit':
        amount = int(input('the deposited money is: '))
        balance += amount
        print('deposit is succeffully') 

    elif action == 'withdrwal':
        amount = int(input('enter amount ro withdraw: '))
        if amount > balance:
            print('invalid')
        else:
            balance -= amount
            print('withdraw  successful')

    elif action == 'exit':
        print('thank you')

    else:
        print('try again.')   


