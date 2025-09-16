class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## creating a range that will then act as True or False
        def bananas_complete(piles,eat_speed):
            output=sum(math.ceil(pile/eat_speed) for pile in piles)
            return output<=h
        ## creating a range equivalent to False, False, False, True , true, true ....    
        left=1
        right=max(piles) 

        while right>left:
            mid=left+((right-left)//2)
            if bananas_complete(piles,mid):
                right=mid
            else:
                left=mid+1
        return left               


        