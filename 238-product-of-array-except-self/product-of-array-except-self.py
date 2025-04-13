class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        prefix=[]
        postfix=[1 for x in range(len(nums))]
        for x in range(len(nums)):
            if x==0:
                prefix.append(1)
            else:
                prefix.append(nums[x-1]*prefix[x-1])
        #print(prefix)
        postfix=1
        for y in range(len(nums)-1,-1,-1):
            prefix[y]*=postfix
            postfix*=nums[y]       
        print(prefix)
        return prefix   
                 
        # for y in range(len(nums)-1,-1,-1):
        #     if y ==len(nums)-1:
        #         postfix[y]=1
        #     else:
        #         postfix[y]=postfix[y+1]*nums[y+1]
        # #print(postfix)    
        # for x in range(len(nums)):
        #     output.append(prefix[x]*postfix[x])
        # return output            