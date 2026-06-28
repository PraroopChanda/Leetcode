class Twitter:

    def __init__(self):

        self.followers=defaultdict(set)
        self.tweetmap=defaultdict(list)
        self.count=0 ## this is important as this will be used for keeping a track of when 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweetmap:
            self.tweetmap[userId].append((tweetId,self.count)) ## tweet,tweet_number(used for getting latest)
        else:
            list_1=[]
            list_1.append((tweetId,self.count))
            self.tweetmap[userId]=list_1        

        self.count-=1 ## because we are using min heap for max , taking negative    

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        min_heap=[]
        self.followers[userId].add(userId) ## because i follow myself as well

        for followeId in self.followers[userId]: ## take the latest first, basically the last added for each one
            len_1=len(self.tweetmap[followeId])
            if len_1!=0:
                tweetID,count=self.tweetmap[followeId][-1] ## basically i am getting the latest from all followers
                min_heap.append([count,tweetID,followeId,len_1-2]) ## tweetcount, tweetID,next index to use

        heapq.heapify(min_heap)
        k=10
        while min_heap and k:
            _,tweetID,followeId,index=heapq.heappop(min_heap)
            res.append(tweetID)
            if index>-1:
                tweetID,count=self.tweetmap[followeId][index]
                heapq.heappush(min_heap,[count,tweetID,followeId,index-1])
            k-=1    

        return res               


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].add(followeeId)
        else:
            frs=set()
            frs.add(followeeId)
            self.followers[followerId]=frs    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)