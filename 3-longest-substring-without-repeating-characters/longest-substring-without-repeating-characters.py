class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1    
        left=0
        right=0
        list_1=[]
        max_len=0
        while left<=right and right<len(s):
            if not list_1:
                list_1.append(s[right])
                max_len=max(max_len,len(list_1))
                right+=1
            elif s[right] not in list_1:
                list_1.append(s[right])
                max_len=max(max_len,len(list_1))
                right+=1
            else:
                while left<right and s[left]!=s[right]:
                    del(list_1[0])
                    left+=1 
                del(list_1[0]) 
                left+=1
        return max_len           
                

                    





        
        