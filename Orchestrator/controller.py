from functions import options, execute_option, parse
from env import commands, Nodes, NodeList, options

print("Nodes Avaible    ", NodeList)
print("Commands Avaible ", commands)

while(1):

    command = input()
    
    if command in options:
        execute_option(command)
    else:
        msg = parse(command)
        print(msg)

