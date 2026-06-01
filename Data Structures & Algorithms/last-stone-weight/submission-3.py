class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            first, second = heapq.heappop_max(heap), heapq.heappop_max(heap)

            if first == second:
                continue
            
            if second < first:
                heapq.heappush_max(heap, first - second)
        
        heapq.heappush_max(heap, 0)
        return heap[0]