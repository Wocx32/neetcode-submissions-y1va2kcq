class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        countT = defaultdict(int)

        for c in t:
            countT[c] = 1 + countT[c]
            
        need = len(countT)

        win = defaultdict(int)
        having = 0

        res, resLen = "", float('inf')

        l = 0
        for r in range(len(s)):

            char = s[r]
            win[char] = 1 + win[char]
        
            if char in countT and win[char] == countT[char]:
                having += 1

            print(need, having, char, char in countT, win[char], countT[char])

            while having == need:

                if (r - l + 1) < resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                
                win[s[l]] -= 1

                if s[l] in countT and win[s[l]] < countT[s[l]]:
                    having -= 1
                
                l += 1
        
        return res