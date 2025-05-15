class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #output_list=[]
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
        #### --------------##########
        # def checkleft(i):
        #     if nums[i]<nums[max(0,i-1)]:
        #         return False
        #     return True
        # def checkRight(i):
        #     if nums[i]<nums[min(len(nums)-1,i+1)]:
        #         return False
        #     return True

        # for x in range(len(nums)):
        #     if checkleft(x) and checkRight(x):
        #         output_list.append(x)
        #         break
        # return output_list[0] 


        ## trying to do using binary search log(n) solution
        ## start looking on the other half, reducing the search space
        l=0
        r=len(nums)-1
        while l<=r:
            mid =(l+r)//2  ##mid is the element that is being now used for comparison
            if mid>0 and nums[mid]<nums[mid-1]: ## logic is basically we will always have a bigger element
                ## change right 
                r=mid-1
            elif mid < len(nums)-1 and nums[mid]<nums[mid+1]: 
                l=mid+1
            else:
                return mid



                
            


        