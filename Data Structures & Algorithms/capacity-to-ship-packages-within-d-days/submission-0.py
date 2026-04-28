class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)
        res = r

        def can_ship(weight):
            days_taken = 1

            capacity = weight
            for w in weights:
                if capacity - w < 0:
                    days_taken += 1
                    if days_taken > days:
                        return False
                    capacity = weight
                capacity -= w
            
            return True

        while l <= r:
            mid = (l + r) // 2

            if can_ship(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
    