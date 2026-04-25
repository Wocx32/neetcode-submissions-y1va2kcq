class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.entries = {}
        self.capacity = capacity
        
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        if self.entries.get(key):
            self.remove_node(self.entries[key])
            self.insert_node(self.entries[key])
            return self.entries[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)

        if self.entries.get(key):
            self.remove_node(self.entries[key])
        
        self.insert_node(node)
        self.entries[key] = node

        if len(self.entries) > self.capacity:
            last = self.tail.prev
            del self.entries[last.key]
            self.remove_node(last)


    def remove_node(self, node: Node) -> None:
        
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.next = None
        node.prev = None
    
    def insert_node(self, node: Node) -> None:

        prev = self.head
        next = self.head.next

        prev.next = node
        next.prev = node

        node.prev = prev
        node.next = next
    