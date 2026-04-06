class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i, char in enumerate(s):
            next_s = ""

            if i < (len(s) - 1):
                next_s = s[i + 1]   


            if char == "I" and (next_s == 'V' or next_s == "X"):
                total -= roman_to_int[char]
            elif char == "X" and (next_s == 'L' or next_s == 'C'):
                total -= roman_to_int[char]
            elif char == "C" and (next_s == 'D' or next_s == 'M'):
                total -= roman_to_int[char]
            else:
                total += roman_to_int[char]
        
        return total

            