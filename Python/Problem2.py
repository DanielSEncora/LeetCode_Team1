#LRU Cache
class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.length = 0
        self.startNode = None
        self.endNode = None

    def get(self, key: int) -> int:
        if key in self.map.keys():
            node = self.map[key]
            self.pushToLast(node)
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.length > 0 and key in self.map.keys():
            node = self.map[key]
            node.val = value
            self.pushToLast(node)
            return
        self.insertNode(key, value)

    def pushToLast(self, node: Node):
        if node.next == None:
            return

        if node.prev == None:
            self.startNode = node.next

        if node.prev == None:
            node.next.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = self.endNode
        node.next = None
        self.endNode.next = node
        self.endNode = node

    def soloNode(self, node: Node):
        self.startNode = node
        self.endNode = node
    
    def insertNode(self, key: int, value: int):
        node = Node(key, value)
        if self.length < self.capacity:
            if self.length == 0:
                self.soloNode(node)

            else:
                self.endNode.next = node
                node.prev = self.endNode
                self.endNode = node

            self.map[key] = node
            self.length += 1
        else: 
            del self.map[self.startNode.key]
            if self.capacity == 1:
                self.soloNode(node)
            else:
                
                self.startNode = self.startNode.next
                self.startNode.prev = None

                
                self.endNode.next = node
                node.prev = self.endNode
                self.endNode = node
            
            self.map[key] = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)