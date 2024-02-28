import sys
import requests
from env import commands, Nodes, NodeList, options

def execute_option(command):

    match(command):
        case 'info':
            print('## Nodes saved in Environments ##')
            for node in Nodes:
                print(Nodes[node]['id'],'\t',Nodes[node]['ip'],'\t',Nodes[node]['port'])
        case 'quit':
            sys.exit("Quitting...")



def start(node):
    
    url = "http://"+Nodes[node]['ip']+":"+Nodes[node]['port']+""
    print("Sending Request to ", url)
    headers = {
        'Content-Type': 'text/html',
        'charset': 'utf-8'
    }
    data = "start"
    msg = requests.post(url,data, headers)

    return msg.text


def stop(node):
    
    url = "http://"+Nodes[node]['ip']+":"+Nodes[node]['port']+""
    print("Sending Request to ", url)
    headers = {
        'Content-Type': 'text/html',
        'charset': 'utf-8'
    }
    data = "stop"
    msg = requests.post(url,data, headers)
    return msg.text


def parse(command):

    split = command.split()

    if len(split) != 2:
        return "Syntax invalid"

    cmd = command.split()[0]
    node = command.split()[1]

    if cmd not in commands:
        return "Command invalid"
    if node not in NodeList:
        return "Node name invalid"
        
    match cmd:
        case 'start':
            msg = start(node)
        case 'stop':
            msg = stop(node)

    return msg
