class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len=len(matrix)
        col_len=len(matrix[0])

        row_zero=False ## basically a flag for checking if first row is zero

        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        row_zero=True

        ## now make zeros on basis of these, but have to start from 1 and not 0, because i have one overlapping element
        for r in range(1,row_len):
            for c in range(1,col_len):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0 ## basically making that element as 0

        if matrix[0][0]==0: ## checking if that column needs to be made as 0
            for r in range(row_len):
                matrix[r][0]=0

        if row_zero: ## make the first row as zero
            for c in range(col_len):
                matrix[0][c]=0


              





        # row_len=len(matrix)
        # col_len=len(matrix[0])
        
        # def makezero(row,col):
        #     for c in range(col_len): ## making all rows 0
        #         matrix[row][c]=0
        #     for r in range(row_len): ## making all cols 0
        #         matrix[r][col]=0   

        # hashmap={}
        # for r in range(row_len):
        #     for c in range(col_len):
        #         if matrix[r][c]==0:
        #             hashmap[(r,c)]=0

        # for keys in hashmap:
        #     r,c=keys
        #     makezero(r,c)


        