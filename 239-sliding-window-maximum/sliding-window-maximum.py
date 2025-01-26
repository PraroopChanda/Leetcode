class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        que=collections.deque() 
        left=right=0
        while right<len(nums): 
            while que and nums[que[-1]]<nums[right]:
                que.pop()
            que.append(right) ## storing the index this time and this will be in decreasig order of nums
            
            ##  need to remove the left element not in the window 
            if left>que[0]: ## because que stores indices
                que.popleft()
                #del que[0]

            if (right+1>=k): ## This will make the window 
                output.append(nums[que[0]]) ## left most element would be the greatest
                left+=1
            right+=1    
        return output        


