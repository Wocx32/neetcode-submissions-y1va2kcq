class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        bins = defaultdict(list)

        for s in strs:
            key = [0] * 26

            for i in s:
                idx = ord(i) - ord('a')
                key[idx] += 1
            
            bins[tuple(key)].append(s)
        
        return [v for v in bins.values()]
