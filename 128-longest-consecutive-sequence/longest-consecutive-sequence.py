class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict_1={}
        for x in nums: ## one pass
            dict_1[x]=set()
        ## next pass
        longest=0
        for y in dict_1:
            if y-1 not in dict_1:
                length=0
                while (y+length) in dict_1.keys():
                    length+=1
                longest=max(longest,length)
        return longest            

                



        