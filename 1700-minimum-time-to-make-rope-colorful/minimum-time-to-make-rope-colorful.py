class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors)==1:
            return 0
        stack=[]
        total_time=0
        for idx,value in enumerate(colors):
            if len(stack)==0:
                stack.append((idx,value))
            elif value == stack[-1][1]:
                if neededTime[idx]>=neededTime[stack[-1][0]]:
                    total_time+=neededTime[stack[-1][0]]
                    stack.pop()
                    stack.append((idx,value))
                else:
                    total_time+=neededTime[idx]
            else:
                stack.append((idx,value))  
        return total_time                    
        