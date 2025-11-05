class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xsum(arr,x)-> int:
            freq=x
            sum1=0
            dict_1={}
            arr=sorted(arr)
            for x in arr:
                dict_1[x]=1+dict_1.get(x,0)
            dict_1=dict(sorted(dict_1.items(),key=lambda x:x[1]))
            keys_list=list(dict_1.keys())
            for keys in range(len(keys_list)-1,-1,-1):
                sum1+=keys_list[keys]*dict_1[keys_list[keys]]
                freq-=1
                if freq==0:
                    break
            return sum1
        output=[]
        for i in range(len(nums)-k+1):
            output.append(xsum(nums[i:i+k],x))
        return output                



        
        