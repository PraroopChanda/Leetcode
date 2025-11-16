class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=set()
        sol=[]
        length=len(candidates)

        def combsum2(sol,idx):
            ## base case
            if sum(sol)==target:
                result.add(tuple(sol[:]))
                return 

            prev=-1 ## at same depth it should not pick the same element ( will/can lead to same solutins again and save recursion as well )
            for elem in range(idx,length):
                if candidates[elem]!=prev and sum(sol)+candidates[elem]<=target:
                    prev=candidates[elem]
                    sol.append(candidates[elem])
                    combsum2(sol,elem+1)
                    sol.pop()

        combsum2(sol,0)
        return [list(elem) for elem in result]               


        