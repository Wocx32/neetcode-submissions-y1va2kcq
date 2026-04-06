class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.followees = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        n = 0
        minHeap = []

        self.followees[userId].add(userId)
        for followee in self.followees[userId]:
            if len(self.posts[followee]) > 0:
                index = len(self.posts[followee]) - 1
                count, tweetId = self.posts[followee][index]
                heapq.heappush(minHeap, [count, tweetId, followee, index])


        while minHeap and n < 10:
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            n += 1

            if index > 0:
                count, tweetId = self.posts[followee][index - 1]
                heapq.heappush(minHeap, [count, tweetId, followee, index - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)        
