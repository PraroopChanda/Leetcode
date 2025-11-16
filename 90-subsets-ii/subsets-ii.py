class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()
        sol=[]
        n=len(nums)

        def dfs(sol,index):
            ## base case
            if index==n: ## reached the max depth
                result.add(tuple(sol[:]))
                return 

            ## left --> not adding anything
            dfs(sol,index+1) ## incrementing the level by 1

            ## right --> adding one element
            sol.append(nums[index])
            dfs(sol,index+1)
            sol.pop() # for bactracking now , we need to pop that elemenet as well

        dfs(sol,0)
        return [list(elem) for elem in result]        
        