class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        stack = []


        for idx, height in enumerate(heights):
            cur_idx = idx
            while stack and stack[-1][1] >= height:
                item = stack.pop()
                max_area = max(max_area, item[1] * (idx - item[0]))
                cur_idx = item[0]
            
            stack.append([cur_idx, height])
        
        while stack:
            item = stack.pop()
            max_area = max(max_area, item[1] * (len(heights) - item[0]))
        
        return max_area