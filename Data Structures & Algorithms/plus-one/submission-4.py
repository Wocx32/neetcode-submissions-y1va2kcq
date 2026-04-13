class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        carry = 1

        for i in range(len(digits) - 1, -1, -1):

            s = digits[i] + carry

            res.append(s % 10)
            carry = s // 10
        
        if carry:
            res.append(carry)

        res.reverse()
        return res
