class RandomizedSet:

    def __init__(self):
        self.indexmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.indexmap:
            return False
        
        self.array.append(val)
        self.indexmap[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexmap:
            return False
        
        idx = self.indexmap[val]
        last = self.array[-1]

        self.array[idx] = last
        self.indexmap[last] = idx
        self.array.pop()
        del self.indexmap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()