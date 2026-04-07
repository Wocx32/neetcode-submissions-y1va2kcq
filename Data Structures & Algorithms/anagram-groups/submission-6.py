class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)


        for s in strs:

            key = str(sorted(s))
            group[key].append(s)
        
        return [l for l in group.values()]
        
