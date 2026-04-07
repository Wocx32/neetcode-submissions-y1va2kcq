class DoublyLinkedNode:
    def __init__(self, key = None, value=None):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DoublyLinkedNode() # sentinel node
        self.tail = DoublyLinkedNode() # sentinel node

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if self.cache.get(key):
            node = self.cache[key]

            self.remove_node(node)
            self.insert_node(node)

            return node.value

        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if self.cache.get(key):
            self.remove_node(self.cache[key])

        node = DoublyLinkedNode(key, value)
        self.cache[key] = node
        self.insert_node(node)

        
        if len(self.cache) > self.capacity:
            node = self.tail.prev

            self.remove_node(node)
            del self.cache[node.key]
        
    
    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        node.next = None
        node.prev = None
    
    def insert_node(self, node):
        first = self.head.next
        self.head.next = node
        first.prev = node

        node.prev = self.head
        node.next = first
