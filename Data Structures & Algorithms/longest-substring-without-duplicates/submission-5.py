class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        contains = set()

        l = 0
        res = 0

        for r in range(len(s)):

            char = s[r]

            while char in contains:
                contains.remove(s[l])
                l += 1
            
            contains.add(char)

            if (r - l + 1) > res:
                res = (r - l + 1)
            
        
        return res