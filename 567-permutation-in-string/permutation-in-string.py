class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## going for a fixed length solution 
        len1=len(s1)
        dict1={}
        for x in s1:
            dict1[x]=1+dict1.get(x,0)    
        dict2={}
        for y in s2[0:len1]:
            dict2[y]=1+dict2.get(y,0)   
        if dict1==dict2:
            return True    
        for x in range(len(s2)-len1):
            dict2[s2[x]]-=1
            if dict2[s2[x]]==0:
                del dict2[s2[x]] 
            dict2[s2[x+len1]]=1+dict2.get(s2[x+len1],0) 
            if dict2==dict1:
                return True
        return False   