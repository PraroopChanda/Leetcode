class Twitter:
    def __init__(self):
        self.time=0 ## will be taking negative values to build a max heap
        self.tweetmap=defaultdict(list) ## (userID: [time,tweetId])
        self.followermap=defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.time,tweetId])
        self.time-=1 ## will be taking negative values to build a max heap
        if userId==2:
            print(self.tweetmap[2])
    def getNewsFeed(self, userId: int) -> List[int]:
        output=[]
        self.followermap[userId].add(userId) ## because we want to consider tweets for the same user Id as well
        max_heap=[]
        for followeeid in self.followermap[userId]:
            if followeeid in self.tweetmap: ## basically if it made any tweets
                last_index=len(self.tweetmap[followeeid])-1
                time, tweetid=self.tweetmap[followeeid][last_index]
                max_heap.append([time,tweetid,followeeid,last_index-1]) ## adding followeeid and last_index as well to later index more values (going from last to first)
        heapq.heapify(max_heap)
        while max_heap and len(output)<10:
            time,tweetid,followeeid,last_index=heapq.heappop(max_heap)
            output.append(tweetid)
            if last_index>=0: ## meaing more tweets are there for that followee 
                time,tweetid=self.tweetmap[followeeid][last_index]
                heapq.heappush(max_heap,[time,tweetid,followeeid,last_index-1])

        return output       
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followermap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followermap[followerId]:
            self.followermap[followerId].remove(followeeId)
# '''
# LOGIC --> from all the followe list , first take the last index values (that would be the most recent according to that user)
# Next --> put all values in a maxheap and get the most recent value and then also push other value for that followe in that heap
# pushing other values from that followe, will still result in most receent value among followes (because if it not recent it won't be picked)
# '''            
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)