
started = False

print('type help to learn about commands')
while True:
    inp = input('>').lower()
    if inp == 'start':
        if started == True:
            print('the car has already been started')
        elif started == False:
            print('the car has been started')
            started = True
    elif inp == 'stop':
        if started != True:
            print('the car has already been stopped')
        if started == True:
            print('the car has been stopped')
            started = False
    elif inp == 'exit':
        quit()
    elif inp == 'help':
        print(" type 'start' to start the car\n type 'stop' to stop the car \n type 'exit' to quit the game")
    else:
        print('type help')
