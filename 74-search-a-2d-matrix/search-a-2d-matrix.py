class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        ## first doing getting the correct row 
        top=0
        bottom=len(matrix)-1 
        while bottom>=top:
            row=(bottom+top)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else: ## this means the value is within this row which we wanted so break
                break
        ## row== is our needed row
        left=0
        right=len(matrix[0])-1
        while right>=left:
            mid=(right+left)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False                        





        