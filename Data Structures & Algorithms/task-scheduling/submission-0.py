class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [cnt for cnt in count.values()]
        heapq.heapify_max(max_heap)
        queue = collections.deque()

        time = 0

        while max_heap or queue:
            time += 1

            if len(max_heap) > 0:
                cnt = heapq.heappop_max(max_heap) - 1

                if cnt:
                    queue.append([cnt, time + n])
            
            if len(queue) > 0 and queue[0][1] == time:
                heapq.heappush_max(max_heap, queue.popleft()[0])
        
        return time