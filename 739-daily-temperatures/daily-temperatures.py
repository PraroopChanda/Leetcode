class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0 for x in range(len(temperatures))]
        stack_1=[0]
        # for x in range(len(temperatures)):
        #     if len(stack_1)!=0: 
        #         while len(stack_1)!=0 and temperatures[stack_1[-1]]<temperatures[x]:
        #             val=stack_1.pop()
        #             output[val]=x-val
        #         stack_1.append(x)   
        #     else:
        #         stack_1.append(x)

        ####
        for x in range(1,len(temperatures)):
            while stack_1 and temperatures[stack_1[-1]]<temperatures[x]:
                val=stack_1.pop()
                output[val]=x-val
            stack_1.append(x)              
        return output                 
                


        