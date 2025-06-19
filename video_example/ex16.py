contacts = []
while True:
    print('choose the option: ')
    print('1.add contacts')
    print('2.view all contacts')
    print('3.delete contact by name')
    print('4.exit the program')

    choice = input('enter choice: ')

    if choice == '1':
        contact_name = input('add contact name: ')
        phone_number = input('add phone number: ')
        contacts.append({'name': contact_name, 'phone': phone_number})
        print('name and phone number added')

    elif choice == '2':
        if not contacts:
            print('no contact')
        else:
            for contact_name,phone_number in enumerate (contacts):
                print(f'{contact_name}.{phone_number}')        

    elif choice == '3':
        if not contact_name:
            print('no contact')
        else:
           for i,contact_name in enumerate (contacts):
                print(f'{contact_name}')   

    elif choice == '4':
        print('exit')
        break

    else:
        print('invalid choice, try again')
                           