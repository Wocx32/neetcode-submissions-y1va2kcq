class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        dp = {}

        def dfs(i):

            if i == len(s):
                return [""]

            if i in dp:
                return dp[i]
            

            res = []
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i: i + len(w)] == w):
                    
                    strings = dfs(i + len(w))

                    for substr in strings:
                        sentence = w
                        if substr:
                            sentence += " " + substr
                        res.append(sentence)
            
            dp[i] = res
            return res
            
        
        return dfs(0)