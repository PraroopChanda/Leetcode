class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        sol=[]
        n=len(nums)
        #### DFS ####
        def backtrack(i):
            if i==n: ## base case
                result.append(sol[:])
                return 

            backtrack(i+1) ## left case

            ## right case (basically adding the elemenet before hand ---> as it would be i==n and return)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()   

        backtrack(0)     

        return result    
                
        