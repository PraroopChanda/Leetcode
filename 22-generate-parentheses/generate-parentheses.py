class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## doing using recursion 
        ## logic is closedN<openN (closed paranthesis should always be less than open      paranthesis)
        ## for generation of different combinations use backtracking -- important observation
        res=[]
        stack1=[]
        def backtracking(openN,closeN):
            if openN==closeN==n:
                res.append("".join(stack1))
                return
            if openN<n:
                stack1.append("(")
                backtracking(openN+1,closeN)
                stack1.pop() ## this is necessary for generating combinations
                ## like last in first out
                ## basically after this -- next combinations starts
            if closeN<openN:
                stack1.append(")")
                backtracking(openN,closeN+1)
                stack1.pop()
        backtracking(0,0)
        return res   