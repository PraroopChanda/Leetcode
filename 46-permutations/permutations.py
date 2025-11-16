class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        sol=[]
        length=len(nums)

        def perm(sol):
            if len(sol)==length:
                result.append(sol[:])
                return

            for elem in nums:
                if elem not in sol:
                    sol.append(elem)
                    perm(sol)
                    sol.pop()

        perm(sol)
        return result            

        