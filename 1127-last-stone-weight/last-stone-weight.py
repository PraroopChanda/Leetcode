class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for x in range(len(stones)):
            stones[x]=-stones[x]
        heapq.heapify(stones)
        stone_len=len(stones)
        while stone_len>1:
            stone1,stone2=heapq.heappop(stones),heapq.heappop(stones)
            if stone1==stone2:
                stone_len-=2
            else:
                heapq.heappush(stones,-abs(stone1-stone2))
                stone_len-=1
        if stones:
            return -stones[0]
        else:
            return 0            


            



        