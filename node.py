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
            listOfServers = node.get_all_servers([], node, 0)
            listOfServers.sort(key = lambda x: x.id)
            self.successor = node.find_node_with_key(listOfServers, self.id)
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
    
    def find_node_with_key(self, listOfServers, key):
        key = key % 256
        if key > listOfServers[-1].id:
            return listOfServers[0]
        start = 0
        end = len(listOfServers)
        while (start<=end):
            mid = (start+end)//2
            if key == listOfServers[mid].id:
                return listOfServers[mid]
            elif key < listOfServers[mid].id:
                end = mid-1
            elif key>listOfServers[mid].id:
                start = mid+1
        return listOfServers[start]
    
    def updateFingerTable(self):
        listOfServers = self.get_all_servers([], self, 0)
        listOfServers.sort(key = lambda x: x.id)
        for server in listOfServers:
            for k in range(8):
                check_val = server.id + 2**k
                server.fingerTable.set(k, self.find_node_with_key(listOfServers, check_val))

    def find(self, key):
        pass

    def insert(self, key, value):
        if value:
            value = int(value)
        listOfServers = self.get_all_servers([], self, 0)
        listOfServers.sort(key = lambda x: x.id)
        dest_node = self.find_node_with_key(listOfServers, key)
        dest_node.localKeys[key] = value

    # def insert_search_fingerTable(self, key, value):
    #     if key == self.id:
    #         self.insert(key, value)
    #     if key < self.id:
    #         offset = 256 - self.id + key
    #     else:
    #         offset = key - self.id
    #     two_power_count = -1
    #     while offset:
    #         offset = offset//2
    #         two_power_count += 1
    #     key_node = self.fingerTable.get(two_power_count)
    #     if key_node.predecessor.id < key:
    #         if key_node.successor.id > key:
    #             key_node.successor.insert(key, value)
    #         else:
    #             key_node.insert(key, value)
    #     else:
    #         key_node.insert_search_fingerTable(key, value)
    
    # def insert(self, key, value):
    #     if value:
    #         value = int(value)
    #     self.localKeys[key] = value

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
