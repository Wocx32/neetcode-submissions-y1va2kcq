class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        left = [-1] * n
        for i in range(n):

            while stack and (heights[i] <= heights[stack[-1]]):
                stack.pop()
            
            if stack:
                left[i] = stack[-1]

            stack.append(i)
        
        stack = []
        right = [n] * n

        for i in range(n - 1, -1, -1):

            while stack and (heights[i] <= heights[stack[-1]]):
                stack.pop()
            
            if stack:
                right[i] = stack[-1]
            
            stack.append(i)
        
        maxArea = 0
        for i in range(n):
            left[i] += 1
            right[i] -= 1
            area = heights[i] * (right[i] - left[i] + 1)
            maxArea = max(maxArea, area)
        return maxArea