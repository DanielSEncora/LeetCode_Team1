#LRU Cache
class Node:
        def __init__(self, key = None, val = None):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

class LRUCache:
    

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.length = 0
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.outAndConnect(node)
        self.insertAtHead(node)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        secondToLast = self.tail.prev
        if key not in self.map: #if the key doesnt exist
            if self.length < self.capacity:
                self.insertAtHead(node)
                self.map[key] = node
                self.length += 1
            else:
                self.outAndConnect(secondToLast)
                self.insertAtHead(node)
                print(key)
                print('second' ,secondToLast.key)
                del self.map[secondToLast.key]
                self.map[key] = node
            return

        duplicate = self.map[key]
        self.outAndConnect(duplicate)
        self.insertAtHead(node)
        self.map[key] = node


    def insertAtHead(self, node: Node):
        secondToFirst = self.head.next
        secondToFirst.prev = node
        node.next = secondToFirst
        node.prev = self.head
        self.head.next = node
    
    def outAndConnect(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)