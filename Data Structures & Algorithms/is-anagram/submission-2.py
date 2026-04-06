class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashm_s = {}
        hashm_t = {}
        
        for i in range(len(s)):
            hashm_s[s[i]] = 1 + hashm_s.get(s[i], 0)
            hashm_t[t[i]] = 1 + hashm_t.get(t[i], 0)
        
        return hashm_s == hashm_t