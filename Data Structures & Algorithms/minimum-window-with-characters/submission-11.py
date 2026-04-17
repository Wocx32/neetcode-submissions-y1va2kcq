class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        l = 0
        res = ""
        resLen = float('inf')
        winCount = {}
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
            
        have = 0
        need = len(tCount)


        
        
        for r in range(len(s)):

            winCount[s[r]] = winCount.get(s[r], 0) + 1
            if s[r] in tCount and winCount[s[r]] == tCount[s[r]]:
                have += 1
            
            while have == need:
                
                if (r - l + 1) < resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                winCount[s[l]] -= 1
                if s[l] in tCount and winCount[s[l]] < tCount[s[l]]:
                    have -= 1

                l += 1


        return res 