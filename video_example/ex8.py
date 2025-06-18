command = ""
started = False
while True :
    command = input('> ')
    if command == 'start' :
         if started :
             print('car is already started')
         else:
             started = True
             print('start - car is ready to go')
    elif command == 'stop':
         if not started :
             print('car is already stopped')
         else:
             started = False
             print('stop - car is stopped')
    elif command == 'help':
         print('''
start - to start a car
stop - to stop a car
quit - to exit
''')     
    elif command == 'quit':
        break
    else:
     print("i don't understand that")
            
         