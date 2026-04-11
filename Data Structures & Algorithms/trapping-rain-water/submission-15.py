class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftmax = rightmax = 0
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:

            if height[l] < height[r]:
                amount = leftmax - height[l]
                res += max(0, amount)
                leftmax = max(leftmax, height[l])
                l += 1
            else:
                amount = rightmax - height[r]
                res += max(0, amount)
                rightmax = max(rightmax, height[r])
                r -= 1
        
        return res