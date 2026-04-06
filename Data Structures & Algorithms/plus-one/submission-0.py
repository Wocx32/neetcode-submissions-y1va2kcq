class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1

        digits = digits[::-1]

        for i in range(len(digits)):
            if carry == 0:
                break

            if digits[i] < 9:
                digits[i] += 1
                carry -= 1

            else:
                digits[i] = 0

        if carry == 1:
            digits.append(1)
        
        return digits[::-1]