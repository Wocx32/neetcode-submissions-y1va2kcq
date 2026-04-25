class MyHashMap:

    def __init__(self):
        self.array = [None] * 10
        self.capacity = 10
        self.tombstone = object()
        self.items = 0

    def _probe(self, key) -> (int, bool):
        index = key % self.capacity
        last_tombstone = -1

        while self.array[index] != None:

            if self.array[index] != self.tombstone and self.array[index][0] == key:
                return index, True

            if self.array[index] == self.tombstone and last_tombstone == -1:
                last_tombstone = index

            index = (index + 1) % self.capacity

        return index if last_tombstone == -1 else last_tombstone, False

    def put(self, key: int, value: int) -> None:
        
        index, found = self._probe(key)
        self.array[index] = [key, value]
        self.items += 1

        if self.items / len(self.array) > 0.7:
            self._resize()


    def get(self, key: int) -> int:
        
        index, found = self._probe(key)
        if found:
            return self.array[index][1]
        return -1

    def remove(self, key: int) -> None:
        
        index, found = self._probe(key)
        if found:
            self.array[index] = self.tombstone
            self.items -= 1

    def _resize(self) -> None:
        old_array = self.array
        old_capacity = self.capacity

        self.capacity = old_capacity * 2
        self.array = [None] * self.capacity
        self.items = 0

        for entry in old_array:
            if entry == None or entry == self.tombstone:
                continue
            
            self.put(entry[0], entry[1])
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)