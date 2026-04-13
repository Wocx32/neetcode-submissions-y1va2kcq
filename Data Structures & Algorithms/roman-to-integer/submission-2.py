class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        
        for i, char in enumerate(s):
            if i < len(s) - 1 and s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                res -= 1

            elif i < len(s) - 1 and s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                res -= 10                    

            elif i < len(s) - 1 and s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                res -= 100
            
            else:
                res += mapping[char]
        
        return res