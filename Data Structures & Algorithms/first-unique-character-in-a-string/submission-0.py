class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = {}

        for idx, i in enumerate(s):
            if count.get(i) != None:
                count[i] = -1
            else:
                count[i] = idx
        
        for i in s:
            if count[i] != -1:
                return count[i]
        
        return -1