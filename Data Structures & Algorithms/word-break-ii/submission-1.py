class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        wordDict = set(wordDict)

        def dfs(i, currStr):

            if i == len(s):
                res.append(currStr)
                return
            
            
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i: i + len(w)] == w):
                    if not currStr:
                        dfs(i + len(w), w)
                    else:
                        dfs(i + len(w), currStr + " " + w)
            
        
        dfs(0, "")
        return res