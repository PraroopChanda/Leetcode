class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_square(num:int):
            sq_sum=0
            for x in str(num):
                sq_sum+=int(x)**2
            return sq_sum
        visited=set()
        visited.add(n)
        sq_num=sum_square(n)
        while sq_num!=1:
            if sq_num in visited:
                return False
            else:
                visited.add(sq_num)
                sq_num=sum_square(sq_num)
        return True        


        