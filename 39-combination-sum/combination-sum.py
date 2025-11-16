class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        sol=[]

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
        print(result)
        return result              
                

        