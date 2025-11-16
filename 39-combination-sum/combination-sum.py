class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        sol=[]

        ### Logic --> Basically to avoid duplicates once we pass on one element in the array
        ## no need to consider it again, because all possible combinations have already been done with it
        ## thats why we use, range(elem,len(candidates))
        def combsum(sol,elem):
            if sum(sol)==target:
                result.append(sol[:])
                return

            for elem in range(elem,len(candidates)):
                if sum(sol)+candidates[elem]<=target:
                    sol.append(candidates[elem])
                    combsum(sol,elem)
                    sol.pop()  
        combsum(sol,0)
        return result              
                

        