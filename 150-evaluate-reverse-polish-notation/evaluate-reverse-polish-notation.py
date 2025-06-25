class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_map={
            "*":lambda x,y:x*y, "/":lambda x,y:x/y,
            "+":lambda x,y:x+y, "-":lambda x,y:x-y
        }
        stack1=[]
        for x in tokens:
            if x in operator_map:
                y=int(stack1.pop())
                stack1[-1]=operator_map[x](int(stack1[-1]),y) 
            else:
                stack1.append(int(x))
        return int(stack1[-1])        
