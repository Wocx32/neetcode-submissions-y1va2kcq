class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        heap = []

        for i, cnt in count.items():
            heapq.heappush(heap, [cnt, i])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while len(heap) != 0:
            res.append(heapq.heappop(heap)[1])

        return res