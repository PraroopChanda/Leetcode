class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output={}
        for x in nums:
            if x not in output:
                output[x]=1
            else:
                output[x]+=1
        ## now sorting
        output=dict(sorted(output.items(), key=lambda item:item[1], reverse=True))

        return list(output.keys())[:k]



       

        