class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):

            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue 

            j = i + 1
            k = len(nums) - 1

            while j < k:
                threeSum = a + nums[j] + nums[k]
                if threeSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                
                elif threeSum > 0:
                    k -= 1
                else:
                    j += 1
        
        return res