class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxAmount = 0

        l, r = 0, len(heights) - 1

        while l < r:

            smaller = min(heights[l], heights[r])
            area = smaller * (r - l)

            maxAmount = max(maxAmount, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxAmount