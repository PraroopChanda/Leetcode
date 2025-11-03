class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ## first checking if total sum of gas is less than cost ( then we can't complete the loop)
        if sum(gas)<sum(cost):
            return -1
        start_index=0
        net_sum=0
        x=0
        ### greedy solution, as soon as out net_sum becomes negative we switch to the next element for starting
        ## why this makes sense because if turns negative at any point it means that that index, 
        ## cost[index]>gas[index], thats why no need to check for between elements
        while x<len(gas):
            net_sum=net_sum+gas[x]-cost[x]
            if net_sum<0:
                start_index=x+1
                net_sum=0
            x+=1

        return start_index        


            

        