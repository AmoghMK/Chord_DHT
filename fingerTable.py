class FingerTable:

    def __init__(self, node):
        self.node = node
        self.fingerTable = [None]*8

    def set(self, index, successor):
        self.fingerTable[index] = successor

    def get(self, index):
        return self.fingerTable[index]
    
    def prettyPrint(self):
        print("----------Node id: {}----------".format(str(self.node.id)))
        print("Successor: {0}, Predecessor: {1}".format(str(self.node.successor.id), str(self.node.predecessor.id)))
        print("FingerTables:")
        for k in range(8):
            print("| {k} [{start}, {end}) \t succ. = {succ_id}".format( 
                k = str(k+1), 
                start = str((self.node.id + 2**k) % 256), 
                end = str((self.node.id + 2**(k+1)) % 256), 
                succ_id = str(self.fingerTable[k].id if self.fingerTable[k] else -1))
            )
        print("--------------------------------")
        print("********************************")
        print()
