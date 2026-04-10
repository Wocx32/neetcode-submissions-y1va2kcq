class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, curr_s):
            if i == len(digits):
                res.append(curr_s)
                return

            
            for char in mapping[digits[i]]:
                backtrack(i + 1, curr_s + char)
        

        backtrack(0, "")
        return res