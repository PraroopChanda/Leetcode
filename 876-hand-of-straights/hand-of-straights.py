class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        sorted_hand=sorted(hand)
        dict_1={}
        list1=[]
        for x in sorted_hand:
            dict_1[x]=1+dict_1.get(x,0)
        no_groups=len(hand)//groupSize
        for _ in range(no_groups):
            groupsize=groupSize
            keys=sorted(list(dict_1.keys())) 
            for key in keys:
                if len(list1)%groupSize!=0 and key!=list1[-1]+1:
                    return False
                list1.append(key)
                dict_1[key]-=1
                if dict_1[key]==0:
                    del dict_1[key]
                groupsize-=1
                if groupsize==0:
                    break
        if len(list1)!=len(hand):
            return False            
        return True                

                    
                



        