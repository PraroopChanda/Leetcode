class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1={}
        for x in s:
            if x in dict_1:
                dict_1[x]+=1
            else:
                dict_1[x]=1
        for y in t:
            if y not in dict_1:
                return False
            else:
                dict_1[y]-=1
        if any(x!=0 for x in dict_1.values()):
            return False        
        return True         