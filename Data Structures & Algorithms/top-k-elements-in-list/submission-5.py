class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        heap = []

        for num, occ in count.items():
            heapq.heappush(heap, (occ, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num[1] for num in heap]