class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)


        for s in strs:

            key = [0] * 26

            for c in s:
                key[ord(c) - ord('a')] += 1

            group[tuple(key)].append(s)
        
        return [l for l in group.values()]
        
