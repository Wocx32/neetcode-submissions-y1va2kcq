class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones
        heapq.heapify_max(self.heap)

        while len(self.heap) > 1:
            first, second = heapq.heappop_max(self.heap), heapq.heappop_max(self.heap)

            if first == second:
                continue
            if second < first:
                heapq.heappush_max(self.heap, first - second)
        
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return 0