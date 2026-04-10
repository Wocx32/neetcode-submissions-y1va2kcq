class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        wordDict = set(wordDict)

        def dfs(i, curr):

            if i == len(s):
                res.append(" ".join(curr))
                return
            
            
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i: i + len(w)] == w):
                    curr.append(w)
                    dfs(i + len(w), curr)
                    curr.pop()
            
        
        dfs(0, [])
        return res