#task manager that can add ,remove,priotoze,save tasks to file
tasks = []
while True:
    action = input('choose the action: ')
    if action == 'add':
        task = input('enter your task:')
        tasks.append(task)
        print(f'the tasks added are:{task}')

    if action == 'remove':
        tasks.pop(task)
        print(f'the removed task are: {task}')

        

        

        
    

