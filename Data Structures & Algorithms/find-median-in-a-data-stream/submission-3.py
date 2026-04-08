class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:

        if self.max_heap and num < self.max_heap[0]:    
            heapq.heappush_max(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.min_heap) - len(self.max_heap) > 1:
            item = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, item)
        elif len(self.max_heap) - len(self.min_heap) > 1:
            item = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, item)
        

    def findMedian(self) -> float:
        
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] + self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return self.max_heap[0]