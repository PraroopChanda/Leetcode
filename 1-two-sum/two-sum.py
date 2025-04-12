class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]
        for x in range(len(nums)-1):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    output.append(x)
                    output.append(y)
                    return output
        