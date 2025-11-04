class Solution:
    def checkValidString(self, s: str) -> bool:
        ## The logic is to keep 2 stack one for left and one for star
        ## if left is empty , we pop from star assuming star be be ")"
        ## now in the case when everything is done, if there are more "("
        ## then we check for "*",if they can act as ")" (condition they shoudl be)
        ## always greater than left index as ")" comes after "(" 
        left_stack=[]
        star_stack=[]
        for idx in range(len(s)):
            if s[idx]=="(":
                left_stack.append(idx)
            elif s[idx]=="*":
                star_stack.append(idx)
            else:
                if len(left_stack)!=0:
                    left_stack.pop()
                elif len(star_stack)!=0:
                    star_stack.pop()
                else:
                    return False         
        if len(left_stack)==0:
            return True
        if len(left_stack)>len(star_stack):
            return False
        for x in range(len(left_stack)-1,-1,-1):
            if left_stack[x]>star_stack[-1]:
                return False
            else:
                left_stack.pop()
                star_stack.pop()
        return True            



        # count={}
        # list_str=list(s)
        # indices=[]
        # for x in range(len(list_str)):
        #     count[list_str[x]]=1+count.get(list_str[x],0)
        #     if list_str[x]=="*":
        #         indices.append(x)
        # for idx in indices:
        #     if count["("]>count[")"]:
        #         list_str[idx]=")"
        #     elif count["("]<count[")"]:  
        #         list_str[idx]="("
        #     else:
        #         list_str[idx]=""             
        # print(list_str)
        # print("pro" if list_str[1] else "roop" )
        # dict_1={")":"("}
        # stack=[]
        # for elem in list_str:
        #     if elem:
        #      if elem not in dict_1:
        #         stack.append(elem)
        #      else:
        #         if len(stack)!=0 and dict_1[elem]==stack[-1]:
        #             stack.pop()
        #         else:
        #             return False
        # print(stack)            
        # if len(stack)==0:
        #     return True
        # else:
        #     return False                    
           


                      



        