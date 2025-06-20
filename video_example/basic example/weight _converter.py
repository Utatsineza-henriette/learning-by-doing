while True:
    weight_input= input('you can enter your weight or exit for stopping : ')
    if weight_input == 'exit':
        exit = input("-do you want to continue? enter yes for continue or q for stopping:")
        if  exit == 'yes':
            continue
        elif exit.lower() == 'q':
            print('you have exited the program')
            break
        else:
            print('thank you for entering your weight')
            break

    if not weight_input.isdigit():
        print('weight must be a number, try again')
        continue


    weight_lbs = int(weight_input)

    if weight_lbs <= 0:
        print("your weight can't be 0 or negative")
        continue
    else:
        kilogram = weight_lbs / 2.205
        print(f'your weight in kilogram is : {kilogram}')
