class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            key = [0] * 26
            
            for c in s:
                index = ord(c) - ord('a')
                key[index] += 1
            
            res[tuple(key)].append(s)

        return [l for l in res.values()]

