class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]: ## a is the target here
                continue ## don't want the same target here
            start_pt, last_pt=i+1,len(nums)-1
            while start_pt<last_pt:
                threesum=a+nums[start_pt]+nums[last_pt]
                if threesum>0:
                    last_pt-=1
                elif threesum<0:
                    start_pt+=1
                else:
                    result.append([a,nums[start_pt],nums[last_pt]])
                    start_pt+=1 ##j is getting incremented
                    last_pt-=1 ## basically last pt should also decrement
                    ## now i have to update the counter
                    while nums[start_pt]==nums[start_pt-1] and start_pt<last_pt:
                        start_pt+=1 ## j repeated is being checked

        return result
        