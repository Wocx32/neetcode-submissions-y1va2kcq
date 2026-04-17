class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        j = 0
        res = 0
        substring = set()

        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[j])
                j += 1
            
            substring.add(s[i])
            res = max(res, i - j + 1)
        
        return res