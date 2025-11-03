class Solution:
    def jump(self, nums: List[int]) -> int:
        ## in this question we basically calculate the jumps going from one range to another
        if len(nums)==1:
            return 0
        l,r=0,0
        farthest=0
        jumps=0
        while r<len(nums)-1:
            for x in range(l,r+1):
                farthest=max(farthest,nums[x]+x)
            l=r+1
            r=farthest
            jumps+=1
        return jumps    


        