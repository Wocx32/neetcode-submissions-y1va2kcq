class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush_max(self.small, num)
        
        if len(self.small) > len(self.large) + 1:
            item = heapq.heappop_max(self.small)
            heapq.heappush(self.large, item)

        if len(self.large) > len(self.small) + 1:
            item = heapq.heappop(self.large)
            heapq.heappush_max(self.small, item)

    def findMedian(self) -> float:
        
        if len(self.small) > len(self.large):
            return self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.small[0] + self.large[0]) / 2.0