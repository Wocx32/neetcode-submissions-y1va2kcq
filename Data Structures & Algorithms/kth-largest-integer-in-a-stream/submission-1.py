class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.cap = k
        self.heap = nums.copy()
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        while len(self.heap) > self.cap:
            heapq.heappop(self.heap)
        
        return self.heap[0]
