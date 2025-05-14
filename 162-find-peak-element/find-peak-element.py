class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        output_list=[]
        # for x in range(1,len(nums)-1):
        #     if nums[x]>nums[x-1] and nums[x]>nums[x+1]:
        #         output_list.append(x)
        # if len(nums)!=1:        
        #     if nums[0]>nums[1]:
        #         output_list.append(0)
        #     if nums[len(nums)-1]>nums[len(nums)-2]:
        #         output_list.append(len(nums)-1)
        # else:
        #     output_list.append(0)   

        def checkleft(i):
            if nums[i]<nums[max(0,i-1)]:
                return False
            return True
        def checkRight(i):
            if nums[i]<nums[min(len(nums)-1,i+1)]:
                return False
            return True

        for x in range(len(nums)):
            if checkleft(x) and checkRight(x):
                output_list.append(x)
                break

        return output_list[0]       

                
            


        