import sys

from utils import *

# maps node name to node objects
node_name_map = {}

# fetch testcase file name from command line argument and read its contents
with open(sys.argv[-1], 'r') as f:
    input_txt = f.read()

inputs = input_txt.split('\n')

# go through each line in testcase file and execute each command serially
for input in inputs:
    
    command = input.split(" ")[0]
    params = input.split(" ")[1:]

    # Creating/Adding a new node:
    if command == "addNode":
        node_name_map[params[0]] = addNode(params[1])

    # Joining a node to DHT:
    elif command == "join":
        if params[1] != 'None':
            newNode = node_name_map[params[0]]
            existingNode = node_name_map[params[1]]
            joinNodes(newNode, existingNode)

    # pretty print fingerTable of a node:
    elif command == "ppf":
        prettyPrintFingerTable(node_name_map[params[0]])

    # insert key into DHT from a given node:
    elif command == "insert":
        node = node_name_map[params[0]]
        key = params[1]
        value = None
        if len(params)==3:
            value = params[2]
        insertKeyValues(node, key, value)

    # pretty print key value pairs stored in a node:
    elif command == "ppk":
        prettyPrintKeyValues(node_name_map[params[0]])

    # look up all keys from a given node:
    elif command == "lookupall":
        lookupall(node_name_map[params[0]])

    # leave a node from DHT:
    elif command == "leave":
        leaveNode(node_name_map[params[0]])
    
    # find value of a key from a given node
    elif command == "find":
        node = node_name_map[params[0]]
        find(node, params[1])

    # remove a key from DHT from a given node
    elif command == "remove":
        node = node = node_name_map[params[0]]
        remove(node, params[1])

exit()
