class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        for num in range(len(digits)-1,-1,-1):
            if carry:
                digits[num]+=carry
                if digits[num]>9:
                    carry=1
                    digits[num]=0
                else:
                    return digits    
            else:
                digits[num]+=1
                if digits[num]<10:
                    return digits
                else:
                    carry=1
                    digits[num]=0
        
        return [1]+digits
        # for num in digits:
        #     digit+=str(num)
        # return [int(num) for num in digit]    
        