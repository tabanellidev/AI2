import sys
import requests
import paramiko
from paramiko import SSHClient
from scp import SCPClient
from env import commands, NodeList, Nodes, options
from users import Users

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

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



def deploy(node):
    
    print("Connection Information: ", Users[node])

    ip = Users[node]['ip']
    port = Users[node]['port']
    user = Users[node]['user']
    password = Users[node]['password']
    path = Users[node]['path']

    ssh = createSSHClient(ip,port, user, password)
    scp = SCPClient(ssh.get_transport())

    scp.put('M1.txt',path)

    msg = "File deployed"

    return msg

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
        case 'deploy':
            msg = deploy(node)

    return msg
