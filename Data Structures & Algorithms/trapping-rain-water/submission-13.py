class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0

        l, r = 0, len(height) - 1
        
        leftMax = height[l]
        rightMax = height[r]


        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water = leftMax - height[l]

                res += water if water > 0 else 0
            
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water = rightMax - height[r]

                res += water if water > 0 else 0

        return res