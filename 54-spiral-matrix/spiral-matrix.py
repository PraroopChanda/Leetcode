class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_len=len(matrix)
        col_len=len(matrix[0])
        if len(matrix)==1 and len(matrix[0])==1:
            return matrix[0]
        ## now solve this 
        output=[]

        left,right=0,col_len
        top,bottom=0,row_len

        while left<right and top<bottom: ## basically until this is met keep going around
            # first going from left to right -> top row
            for c in range(left,right):
                output.append(matrix[top][c]) ## top row
            top+=1

            ## second right most column, top to down
            for r in range(top,bottom):
                output.append(matrix[r][right-1])
            right-=1

            ## third is bottom row
            if not(left<right and top<bottom): ## intermediate check needed (important)
                break
            for c in range(right-1,left-1,-1):
                output.append(matrix[bottom-1][c])
            bottom-=1

            ## fourth is left most column
            for r in range(bottom-1,top-1,-1):
                output.append(matrix[r][left])
            left+=1

        return output                




        