class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(target):
            l = 0
            r = len(nums)
            
            while l < r:
                mid = (l + r) // 2

                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        first = binary_search(target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        
        return [first, binary_search(target + 1) - 1]