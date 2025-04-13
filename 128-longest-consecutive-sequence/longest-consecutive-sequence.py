class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output=1
        dict_1={}
        for x in nums: ## one pass
            dict_1[x]=set()
        ## next pass
        for y in dict_1:
            if y-1 not in dict_1:
                x=1
                while y+x in dict_1:
                    dict_1[y].add(y+x)
                    x+=1
        print(dict_1.values())

        if nums==[]:
            return 0
        print(max(len(s) for s in dict_1.values()))  
        return (max(len(s) for s in dict_1.values()))+1       
        return max(len(dict_1.values()))+1        
                



        