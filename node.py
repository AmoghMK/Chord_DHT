from fingerTable import FingerTable

class Node:
    
    def __init__(self, id):
        self.id = id
        self.fingerTable = FingerTable(self)
        self.localKeys = {}
        self.successor = self
        self.predecessor = self
    
    def join(self, node):
        if node != None:
            self.successor = node.find_node_with_key(self.id)
            self.predecessor = self.successor.predecessor
            self.successor.predecessor = self
            self.predecessor.successor = self
            self.migrateKeys(self.successor)
        self.updateFingerTable()

    def get_all_servers(self, listOfServers, origNode, count):
        if origNode == self and count>0:
            return
        listOfServers.append(self)
        self.successor.get_all_servers(listOfServers, origNode, count+1)
        return listOfServers

    def find_node_with_key(self, key):
        if key == self.id:
            return self
        elif self.predecessor == self == self.successor:
            return self
        elif (self.predecessor.id < key < self.id) or (self.predecessor.id > self.id and key < self.id):
            return self
        elif (self.predecessor.id > self.id and key > self.predecessor.id):
            if self.predecessor == self.successor:
                return self.successor
            return self
        if key < self.id:
            offset = 256 - self.id + key
        else:
            offset = key - self.id
        two_power_count = -1
        while offset:
            offset = offset//2
            two_power_count += 1
        key_node = self.fingerTable.get(two_power_count)
        if key_node.predecessor.id > key and key_node.predecessor == self:
            return key_node.predecessor
        else:
            return key_node.find_node_with_key(key)
    
    def updateFingerTable(self):
        listOfServers = self.get_all_servers([], self, 0)
        listOfServers.sort(key = lambda x: x.id)
        for server in listOfServers:
            for k in range(8):
                check_val = server.id + 2**k
                server.fingerTable.set(k, self.find_node_with_key(check_val))

    def find(self, key):
        pass

    def insert(self, key, value):
        if value:
            value = int(value)
        dest_node = self.find_node_with_key(key)
        dest_node.localKeys[key] = value

    def migrateKeys(self, successor):
        totalKeys = successor.localKeys
        keysToBeDeleted = []
        for key, value in totalKeys.items():
            if key <= self.id:
                print("migrate key {0} from node {1} to node {2}".format(
                    str(key), str(successor.id), str(self.id)))
                self.localKeys[key] = value
                keysToBeDeleted.append(key)
        for key in keysToBeDeleted:
            successor.remove(key)
        print()
                

    def prettyPrint(self):
        print("----------Node id: {}----------".format(str(self.id)))
        print(self.localKeys)
        print()

    def remove(self, key):
        del self.localKeys[key]

    def leave(self):
        self.predecessor.successor = self.successor
        self.successor.predecessor = self.predecessor
        for key, value in self.localKeys.items():
            if key <= self.id:
                print("migrate key {0} from node {1} to node {2}".format(
                    str(key), str(self.successor.id), str(self.id)))
                self.successor.localKeys[key] = value
        print()
        self.successor.updateFingerTable()

    def lookupall(self, origNode, count):
        if origNode == self and count>0:
            return
        if not count:
            print("----------Node id: {}----------".format(str(self.id)))
        path = [origNode.id]
        if origNode != self:
            path.append(self.id)
        for key, value in self.localKeys.items():
            print("Lookup result of key {key} from node {node_id} with path {path} value is {value}".format(
                key = str(key), 
                node_id = str(origNode.id),
                path = str(path),
                value = str(value)
            ))
        self.successor.lookupall(origNode, count+1)
