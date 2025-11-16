class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        sol=""
        opened=n
        closed=n

        def paranthesis(sol,opened,closed):
            if len(sol)==2*n:
                result.append(sol)
                return

            if opened:
                sol+="("
                paranthesis(sol,opened-1,closed)
                sol=sol[:-1]

            if closed>opened:
                sol+=")"
                paranthesis(sol,opened,closed-1)
                sol=sol[:-1]

        paranthesis(sol,opened,closed)
        return result                

