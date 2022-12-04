from node import Node

def addNode(id):
    return Node(int(id))

def joinNodes(newNode, existingNode):
    newNode.join(existingNode)

def prettyPrintFingerTable(node):
    node.fingerTable.prettyPrint()

def prettyPrintKeyValues(node):
    node.prettyPrint()

def insertKeyValues(node, key, value):
    node.insert(int(key), value)

def leaveNode(node):
    node.leave()

def lookupall(node):
    node.lookupall(node, 0)
    print()

def find(node, key):
    node.find(int(key))

def remove(node, key):
    node.findAndRemove(int(key))
