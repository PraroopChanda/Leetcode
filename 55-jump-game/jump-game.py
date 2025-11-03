class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ### iterating from the last index(n-1) and checking if we can reach from there
        if len(nums)==1:
            return True
        target=len(nums)-1
        for x in range(len(nums)-2,-1,-1):
            if nums[x]+x>=target:
                target=x     
        if target==0:
            return True
        else:
            return False            


        