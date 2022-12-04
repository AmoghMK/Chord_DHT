import sys

from utils import *

node_name_map = {}

with open(sys.argv[-1], 'r') as f:
    input_txt = f.read()

inputs = input_txt.split('\n')

for input in inputs:
    
    command = input.split(" ")[0]
    params = input.split(" ")[1:]

    if command == "addNode":
        node_name_map[params[0]] = addNode(params[1])

    elif command == "join":
        if params[1] != 'None':
            newNode = node_name_map[params[0]]
            existingNode = node_name_map[params[1]]
            joinNodes(newNode, existingNode)

    elif command == "ppf":
        prettyPrintFingerTable(node_name_map[params[0]])

    elif command == "insert":
        node = node_name_map[params[0]]
        key = params[1]
        value = None
        if len(params)==3:
            value = params[2]
        insertKeyValues(node, key, value)

    elif command == "ppk":
        prettyPrintKeyValues(node_name_map[params[0]])

    elif command == "lookupall":
        lookupall(node_name_map[params[0]])

    elif command == "leave":
        leaveNode(node_name_map[params[0]])
    
    elif command == "find":
        node = node_name_map[params[0]]
        find(node, params[1])

    elif command == "remove":
        node = node = node_name_map[params[0]]
        remove(node, params[1])

exit()
