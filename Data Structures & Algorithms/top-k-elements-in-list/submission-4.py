class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []

        for num, occ in count.items():
            heapq.heappush(heap, (occ, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [entry[1] for entry in heap]