class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_len=len(board)
        col_len=len(board[0])
        visited=set()
        ## assigning the corner 0's a temporary value T
        def dfs(r,c):
            if r<0 or r>=row_len or c<0 or c>=col_len or board[r][c]=="X" or (r,c) in visited:
                return 
            visited.add((r,c))
            board[r][c]="T"

            dfs(r-1,c)    
            dfs(r+1,c)    
            dfs(r,c-1)    
            dfs(r,c+1)    
        
        for r in range(row_len):
            for c in range(col_len):
                if r in [0,row_len-1] or c in [0,col_len-1] and board[r][c]=="O":
                    dfs(r,c)

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c]=="O":
                    board[r][c]="X"

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c]=="T":
                    board[r][c]="O"                






        # visited=set()
        # val_idx=[]

        # for r in range(row_len):
        #     for c in range(col_len):
        #         if board[r][c]=="O":
        #             val_idx.append((r,c))           

        # def dfs(r,c):
        #     if r <=0 or r>=row_len-1 or c<=0 or c>=col_len-1 or (r,c) in visited or board[r][c]=="X":
        #         return
        #     board[r][c]="X"
        #     visited.add((r,c)) 

        #     dfs (r-1,c)    
        #     dfs (r+1,c)    
        #     dfs (r,c-1)    
        #     dfs (r,c+1) 


        # for (r,c) in val_idx:
        #     dfs(r,c)       


        