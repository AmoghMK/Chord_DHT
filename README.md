**Author:** Amogh Madanayakanahalli Kumar
<br> **Student id:** 2005781
<br> **Email:** amadanay@ucsc.edu
<br><br>

### **Running the code:**
-  ```python3 main.py <test input file>```
 <br>(Ex: ```python3 main.py testcase.txt```)

### **Building Testcase file:**
- testcase file will contain a list of commands with a command in each line.
- each command will have its commandName first, followed by its parameters.
- An example testcase file is included with the project ```testcase.txt```.
- Commands implemented and their format with examples below:
    - *Creating/Adding a new node:*
    <br> addNode <node_name> <node_id> 
        - Ex: ```addNode n1 30```
    - *Joining a node to DHT:*
    <br> join <new_node_name> <existing_node_name>
        - Ex: ```join n1 n0```
    - *pretty print fingerTable of a node:*
    <br> ppf <node_name>
        - Ex: ```ppf n0```
    - *insert key into DHT from a given node:*
    <br> insert <node_name> <key> <value>
        - Ex: ```insert n0 3 3```
    - *pretty print key value pairs stored in a node:*
    <br> ppk <node_name>
        - Ex: ```ppk n0```
    - *look up all keys from a given node:*
    <br> lookupall <node_name>
        - Ex: ```lookupall n2```
    - *leave a node from DHT:*
    <br> leave <node_name>
        - Ex: ```leave n1```
    - *find value of a key from a given node*
    <br> find <node_name> <key>
        - Ex: ```find n0 3```
    - *remove a key from DHT from a given node*
    <br> remove <node_name> <key>
        - Ex: ```remove n1 3```

### **Files:**
- main.py -> main file which needs to executed
- utils.py -> interface for commands in testcase to functionality in node objects.
- node.py -> contains class Node and its methods involved.
- fingerTable.py -> contains class fingerTable and its methods.
