class DLNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.freq = 1

        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self):
        self.head = DLNode()
        self.tail = DLNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

        self.items = 0
    
    def insert_left(self, node):
        next = self.head.next
        self.head.next = node
        next.prev = node

        node.prev = self.head
        node.next = next

        self.items += 1
    
    def remove_node(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.prev = None
        node.next = None

        self.items -= 1
    
    def remove_right(self):
        node = self.tail.prev
        prev = node.prev
        prev.next = self.tail
        self.tail.prev = prev

        node.next = None
        node.prev = None

        self.items -= 1

        return node

    def is_empty(self):
        return self.items == 0

class LFUCache:

    def __init__(self, capacity: int):

        self.map = {}  # key -> node
        self.countmap = defaultdict(LRUCache) # count -> LRU

        self.capacity = capacity
        self.items = 0
        self.lfuCount = 1
        

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            
            self.move_node(node)

            return node.value
        
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.map:
            node = self.map[key]
            node.value = value

            self.move_node(node)

            return
        
        if self.items == self.capacity:
            node = self.countmap[self.lfuCount].remove_right()
            self.map.pop(node.key)
            self.items -= 1
        
        self.lfuCount = 1
        node = DLNode(key, value)
        self.map[key] = node
        self.countmap[self.lfuCount].insert_left(node)
        self.items += 1


    
    def move_node(self, node):

        self.countmap[node.freq].remove_node(node)
        if self.countmap[node.freq].is_empty() and node.freq == self.lfuCount:
            self.lfuCount += 1

        node.freq += 1
        self.countmap[node.freq].insert_left(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)