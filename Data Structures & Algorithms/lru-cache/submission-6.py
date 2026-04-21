class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not self.map.get(key):
            return -1
        
        node = self.map.get(key)
        self.remove_node(node)
        self.insert_node(node)

        return node.val
    


    def put(self, key: int, value: int) -> None:
        
        node = Node(key, value)

        if self.map.get(key):
            self.remove_node(self.map.get(key))
        
        self.map[key] = node

        self.insert_node(node)

        if len(self.map) > self.cap:
            last = self.tail.prev
            del self.map[last.key]
            self.remove_node(last)
        
        
    
    def remove_node(self, node):

        left = node.prev
        right = node.next

        left.next = right
        right.prev = left

        node.prev = None
        node.next = None
    
    def insert_node(self, node):

        left = self.head
        right = self.head.next

        left.next = node
        right.prev = node
        
        node.prev = left
        node.next = right