while True:
    user_input = (input('enter a number: '))
    if user_input == 'exit':
            print('thank you')
            break 
    
    if user_input.isdigit():    
        number = int(user_input)
        if  number % 2 == 0:
            print('the number is even')
        else:
            print('the number is odd') 
    else:
         print('invalid number')   
       