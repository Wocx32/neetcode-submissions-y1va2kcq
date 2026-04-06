class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush_max(heap, num)
        
        while k > 1:
            heapq.heappop_max(heap)
            k -= 1
        
        return heap[0]