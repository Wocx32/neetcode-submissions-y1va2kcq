class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def binary_search(num):
            l = 0
            r = len(nums)

            while l < r:

                mid = (l + r) // 2

                if nums[mid] >= num:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        start = binary_search(target)
        if start == n or nums[start] != target:
            return [-1, -1]
        
        return [start, binary_search(target + 1) - 1]
        
