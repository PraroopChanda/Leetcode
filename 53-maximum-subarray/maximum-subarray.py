class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ## developing a greeedy solution--use some criteria
        max_sum=nums[0]
        current_sum=nums[0]
        temp_start=0
        start=0
        end=0

        ## here the greedy approach is basically always comparig the sum of series with current elemet
        ## if sum is increasing, continue otherwise start new
        for elem in range(1,len(nums)):
            if nums[elem]>(nums[elem]+current_sum):
                current_sum=nums[elem]
                temp_start=elem
            else:
                current_sum+=nums[elem]
            if current_sum>max_sum:
                max_sum=current_sum
                start=temp_start
                end=elem+1

        return max_sum       


        



        