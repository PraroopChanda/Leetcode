class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        start=0
        result=0
        for end in range(len(s)):
            count[s[end]]=1+count.get(s[end],0)
            while (end-start+1)-max(count.values())>k:
                count[s[start]]-=1
                start+=1

            result=max(result,end-start+1) ## end-start+1 is the length of the substring

        return result         
