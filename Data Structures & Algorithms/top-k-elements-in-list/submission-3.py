class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        heap = []

        for num, count in count.items():
            heapq.heappush(heap, (count, num))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        return [i[1] for i in heap]