import sys
import requests
import paramiko
import os
import shutil
from datetime import datetime
from zipfile import ZipFile
from pathlib import Path
from paramiko import SSHClient
from scp import SCPClient
from env import commands, NodeList, Nodes, options

from users import Users
'''
For security reason users.py is not published on Github, but it should contain a json "Users" with the following structure

Users = {
    "nodeid": {
    "user":"test",
    "ip": "127.0.0.1",
    "password":"test",
    "port":"22",
    "path":"/Users/Test/Desktop/"
    },
    ...
}

'''


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

    filename = node + '_' +datetime.now().strftime('%m-%d') + '.zip'

    requirements_path = os.path.join(Path.cwd().parent, 'Node\\requirements.txt')
    listener_path = os.path.join(Path.cwd().parent, 'Node\\actor_listener.py')

    node_path = os.path.join(Path.cwd().parent, 'Node\\Nodes\\'+node)

    worker_path = os.path.join(node_path, 'worker.py')
    env_path = os.path.join(node_path, 'env.py')

    print('Listerner path   ', listener_path)
    print('Worker path      ', worker_path)
    print('Env path         ', env_path)


    with ZipFile(filename, 'w') as zip_object:
        
        zip_object.write(requirements_path, os.path.basename(requirements_path))
        zip_object.write(listener_path, os.path.basename(listener_path))
        zip_object.write(worker_path, os.path.basename(worker_path))
        zip_object.write(env_path, os.path.basename(env_path))

    print('Archive Zip ' + filename + ' created')

    ssh = createSSHClient(ip,port, user, password)
    scp = SCPClient(ssh.get_transport())

    scp.put(filename,path)

    print('Archive Zip ' + filename + ' deployed')

    shutil.move(filename, 'Repository/' + filename)


    msg = "Archive Zip moved into repository"

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
