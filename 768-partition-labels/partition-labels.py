class Solution:
    def partitionLabels(self, s: str) -> List[int]:
            if len(s)==1:
                return s
            dict_1={}
            for x in range(len(s)):
                dict_1[s[x]]=x # capturing the last index (where each character ends)
            output=[]
            elem=""
            farthest=0
            for idx in range(len(s)):
                if len(elem)==0:
                    elem+=s[idx]
                    farthest=dict_1[s[idx]]
                    if farthest == idx:
                        output.append(len(elem))
                        elem=""
                elif farthest>=dict_1[s[idx]] and farthest!=idx:
                    elem+=s[idx]
                elif farthest<dict_1[s[idx]]:
                    elem+=s[idx]
                    farthest=dict_1[s[idx]]
                else:
                    elem+=s[idx]
                    output.append(len(elem))
                    elem=""
            return output              











        