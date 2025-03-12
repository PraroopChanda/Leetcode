class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict_1={}
        for x in nums:
            if x in dict_1.keys():
                return x
            else:
                dict_1[x]=0   
        