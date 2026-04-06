class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.keyStore.get(key):
            self.keyStore[key].append([value, timestamp])
        else:
            self.keyStore[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keyStore:
            return ""
        
        values = self.keyStore.get(key, [])
        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
