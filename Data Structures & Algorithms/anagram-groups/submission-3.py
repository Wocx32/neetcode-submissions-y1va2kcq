class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        bins = {}

        for i in strs:
            key = [0] * 26

            for j in i:
                key[ord(j) - ord('a')] += 1
            
            key = tuple(key)
            
            if bins.get(key):
                bins[key].append(i)
            else:
                bins[key] = [i]
        
        return list(bins.values())