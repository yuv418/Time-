from timer import Timer
while True:
    try:
        cmd = input(':')
        if cmd == 'help':
            print('start: start timer\nexit: exit program')
        elif cmd == 'start':
            a = Timer()
            a.start()
        elif cmd == 'exit':
            print("exited with code: 0")
            exit()
        else:
            print('command: '+ "'" + cmd + "'" + ' not found' )
    except EOFError:
        print('exited with code: 0')
        exit()
