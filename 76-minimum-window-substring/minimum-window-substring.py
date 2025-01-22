class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        dict1={}
        dict2={}
        for x in t:
            dict1[x]=1+dict1.get(x,0)
        tkey,skey=len(dict1),0
        reslen=float("infinity")
        result=[0,0]
        start=0

        for end in range(len(s)):
            dict2[s[end]]=1+dict2.get(s[end],0)
            if s[end] in dict1 and dict2[s[end]]==dict1[s[end]]:
                skey+=1
            while skey==tkey:
                if (end-start+1)<reslen:
                    reslen=end-start+1
                    result=[start,end+1]
                ## pop the start element
                dict2[s[start]]-=1
                if s[start] in dict1 and dict2[s[start]]<dict1[s[start]]:
                    skey-=1
                start+=1           

        return s[result[0]:result[1]] if reslen!=float("infinity") else ""          



            
            
                