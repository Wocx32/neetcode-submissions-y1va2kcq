class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashm_s = {}
        hashm_t = {}
        
        for c in s:
            if hashm_s.get(c):
                hashm_s[c] += 1
            else:
                hashm_s[c] = 1
        
        for c in t:
            if hashm_t.get(c):
                hashm_t[c] += 1
            else:
                hashm_t[c] = 1
        
        return hashm_s == hashm_t