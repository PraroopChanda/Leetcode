class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        sol=[]
        length=len(s)

        def is_palindrome(sol):
            return sol[:]==sol[::-1]

        def dfs(start):
            if start==length:
                result.append(sol[:])
                return 

            for end in range(start+1,length+1):
                substring=s[start:end]
                if is_palindrome(substring):
                    sol.append(substring)
                    dfs(end) ## next element
                    sol.pop()
        dfs(0)
        return result
                    




        