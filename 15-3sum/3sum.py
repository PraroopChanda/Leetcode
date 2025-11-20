class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        length=len(nums)-1
        result=[]
        for idx in range(len(nums)):
            left=idx+1
            right=length
            target=nums[idx]
            if idx>0 and nums[idx]==nums[idx-1]:
                continue    
            while left<right:
                if nums[left]+nums[right]>-target:
                    right-=1
                elif nums[left]+nums[right]<-target:
                    left+=1
                else:
                    result.append([target,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1

        return result     








        