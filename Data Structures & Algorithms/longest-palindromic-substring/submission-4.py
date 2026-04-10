class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = {}
        res = ""

        def isPali(i, j):
            if i >= j:
                return True
            
            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == s[j]:
                dp[(i, j)] = isPali(i + 1, j - 1)
            else:
                dp[(i, j)] = False
            
            return dp[(i, j)]


        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPali(i, j) and (j - i + 1) > len(res):
                    res = s[i:j+1]
        
        return res