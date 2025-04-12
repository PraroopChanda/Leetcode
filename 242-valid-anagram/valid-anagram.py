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
            dict_1[y]-=1    
            if dict_1[y]<0:
                return False
        return all(value==0 for value in dict_1.values())               