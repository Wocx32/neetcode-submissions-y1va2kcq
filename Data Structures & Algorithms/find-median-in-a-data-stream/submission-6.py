class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        
        if self.right_min and num < self.right_min[0]:
            heapq.heappush_max(self.left_max, num)
        else:
            heapq.heappush(self.right_min, num)
        
        if len(self.left_max) - len(self.right_min) > 1:
            val = heapq.heappop_max(self.left_max)
            heapq.heappush(self.right_min, val)
        
        if len(self.right_min) - len(self.left_max) > 1:
            val = heapq.heappop(self.right_min)
            heapq.heappush_max(self.left_max, val)


    def findMedian(self) -> float:
        
        if len(self.left_max) == len(self.right_min):
            return (self.left_max[0] + self.right_min[0]) / 2
        
        elif len(self.left_max) > len(self.right_min):
            return self.left_max[0]
        
        else:
            return self.right_min[0]