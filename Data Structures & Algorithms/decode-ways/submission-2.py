class Solution:
    def numDecodings(self, s: str) -> int:
        
        cache = {len(s): 1}

        def dfs(i):

            if i in cache:
                return cache[i]

            if s[i] == "0":
                cache[i] = 0
                return 0

            res = dfs(i + 1)

            if i + 2 <= len(s) and s[i: i + 2] >= "10" and s[i: i + 2] <= "26":
                res += dfs(i + 2)
            
            cache[i] = res

            return res

        return dfs(0)

