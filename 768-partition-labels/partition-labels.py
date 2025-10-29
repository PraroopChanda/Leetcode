class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s)==1:
            return [1]
        ## logic is we first do one pass through the entire array and record which 
        ## is the last occuring position of that element 
        output=[]
        dict_1={}
        for x in range(len(s)):
            dict_1[s[x]]=x
        ## logic --> one partion's element should not be in next subset
        ## so we keep an end pointer too keep track of max(last element) in the sequence
        ## once that is reached --> split
        seq=""
        end=dict_1[s[0]]
        for elem in range(len(s)):
            if len(seq)==0:
                seq+=s[elem]
                end=dict_1[s[elem]]
                if elem==len(s)-1:
                    output.append(len(seq))
                    return output
            if dict_1[s[elem]]>=end and elem!=end:
                seq+=s[elem]
                end=dict_1[s[elem]]
            elif dict_1[s[elem]]<end:
                seq+=s[elem]
            else:
                seq+=s[elem]
                output.append(len(seq)-1)
                seq=""
        return output    

        ## could have done the same using seq=0 as well and then doing seq+1 at each time    





                



        

            






        