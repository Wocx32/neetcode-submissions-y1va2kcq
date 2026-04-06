class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0

        leftMax = [0] * len(height)
        rightMax = [0] * len(height)


        leftMax[0] = height[0]
        for i in range(1, len(height) - 1):

            leftMax[i] = max(leftMax[i - 1], height[i])
        
        rightMax[-1] = height[-1] 
        for j in range(len(height) - 2, -1, -1):

            rightMax[j] = max(rightMax[j + 1], height[j])

        for idx, i in enumerate(height):
            water = min(leftMax[idx], rightMax[idx]) - i

            res += water if water > 0 else 0

        return res