class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        otstring=""
        for x in s:
            if x not in otstring:
                otstring+=x
            else:
                otstring=otstring[otstring.index(x)+1:]+x
            max_length=max(max_length,len(otstring))

        return max_length  
        