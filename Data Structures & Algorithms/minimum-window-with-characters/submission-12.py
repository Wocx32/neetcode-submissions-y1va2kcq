class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        win = {}
        having = 0
        need = len(countT)
        res = ""
        resLen = float('inf')
        l = 0

        for r in range(len(s)):

            win[s[r]] = win.get(s[r], 0) + 1
            if s[r] in countT and win[s[r]] == countT[s[r]]:
                having += 1


            while having == need:
                if (r - l + 1) < resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                
                if s[l] in countT and win[s[l]] == countT[s[l]]:
                    having -= 1
                
                win[s[l]] -= 1
                l += 1

        return res