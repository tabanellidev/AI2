options = [
    "info",
    "quit",
]

commands = [
    "start",
    "stop",
]

Nodes = {
    "node1": {
    "id":"node1",
    "ip":"192.168.1.59",
    "port":"8080"
    },  
    "node2": {
    "id":"node2",
    "ip":"192.168.1.61",
    "port":"8080"
    },
    "test": {
    "id":"test",
    "ip":"localhost",
    "port":"8080"
    },  
}


NodeList = []

for node in Nodes:
    NodeList.append(node)
