class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        dp = {}    
        def dfs(i):

            if i >= len(s):
                return [""]
            
            if i in dp:
                return dp[i]
            
            res = []

            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:

                    result = dfs(i + len(word))

                    for sen in result:
                        if not sen:
                            res.append(word)
                        else:
                            res.append(word + ' ' + sen)
                    
            dp[i] = res
            return dp[i]

        return dfs(0)