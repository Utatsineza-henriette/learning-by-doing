while True:
    num1 = int(input('enter first number: '))
    num2 = int (input('enter second number: '))
    operation = input('choose the operations(sum/substract/multiply/divide) or exit: )')
    if operation == 'sum':
        sum = num1 + num2
        print(sum)
    
    elif operation == 'substract':
        substract = num1 - num2
        print(substract)

    elif operation == 'multiply':    
        multiply = num1 * num2
        print(multiply)
    
    elif operation == 'divide':
        if num2 == 0:
             print('invalid')
        else:
            divide = num1 / num2
            print(divide)
    
    else:
        break