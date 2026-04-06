class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        found = {}
        res = 0

        l = 0
        for r in range(len(s)):
            
            if s[r] in found:
                l = max(found[s[r]] + 1, l)
            
            res = max(res, r - l + 1)
            found[s[r]] = r
        
        return res