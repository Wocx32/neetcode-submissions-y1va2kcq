class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        l_max = 0
        r_max = 0

        res = 0

        while l <= r:

            if l_max < r_max:
                l_max = max(l_max, height[l])
                res += max(0, l_max - height[l])
                l += 1
            
            else:
                r_max = max(r_max, height[r])
                res += max(0, r_max - height[r])
                r -= 1
        
        return res