class Solution:
    def trap(self, height: List[int]) -> int:
        
        totalWater = 0

        for idx, i in enumerate(height):
            leftMax = 0
            rightMax = 0

            for l in range(0, idx):

                leftMax = max(leftMax, height[l])
            
            for r in range(idx + 1, len(height)):

                rightMax = max(rightMax, height[r])

            water = min(leftMax, rightMax) - i

            if water > 0:
                totalWater += water

        return totalWater