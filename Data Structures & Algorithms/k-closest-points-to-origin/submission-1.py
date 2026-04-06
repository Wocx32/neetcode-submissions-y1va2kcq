class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidean(point):
            return math.sqrt(point[0]**2 + point[1]**2)
        
        heap = []

        for point in points:    
            heapq.heappush_max(heap, [euclidean(point), point])
        
            if len(heap) > k:
                heapq.heappop_max(heap)

        
        return [entry[1] for entry in heap]