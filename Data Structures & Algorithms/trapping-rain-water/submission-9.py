class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0

        leftMax = [0] * (len(height) + 1)
        rightMax = [0] * (len(height) + 1)


        for i in range(len(height) - 1):

            leftMax[i] = max(leftMax[i - 1], height[i])
        
        for j in range(len(height) - 1, -1, -1):

            rightMax[j] = max(rightMax[j + 1], height[j])

        for idx, i in enumerate(height):
            water = min(leftMax[idx], rightMax[idx]) - i

            res += water if water > 0 else 0

        return res