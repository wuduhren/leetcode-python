class Twitter:

    def __init__(self):
        self.followData = collections.defaultdict(set)
        self.tweetData = collections.defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetData[userId].append((self.count, tweetId))
        self.count -= 1

    
    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        h = []
        
        self.followData[userId].add(userId)
        for followeeId in self.followData[userId]:
            if followeeId not in self.tweetData: continue
            index = len(self.tweetData[followeeId])-1
            count, tweetId = self.tweetData[followeeId][index]
            h.append((count, tweetId, followeeId, index-1))
        heapq.heapify(h)
        
        while h and len(newsFeed)<10:
            _, tweetId, userId, index = heapq.heappop(h)
            newsFeed.append(tweetId)
            if index>=0:
                count, tweetId2 = self.tweetData[userId][index]
                heapq.heappush(h, (count, tweetId2, userId, index-1))
        return newsFeed
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followData[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followData: return
        self.followData[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)