from functions import options, execute_option, parse
from env import commands, NodeList, Nodes, options

print("Commands Avaible ", commands)
print("Nodes Avaible    ", NodeList)

while(1):

    command = input()
    
    if command in options:
        execute_option(command)
    else:
        print('------------------------')
        msg = parse(command)
        print(msg)
        print('------------------------')

