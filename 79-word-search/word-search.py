class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ## i being the position of word we are searching
        length=len(word)
        rows=len(board)
        cols=len(board[0])
        path=set()
        
        ### using indices instead of letters and just doing a check for all neighbours
        ### kind of like floodfill algorithm
        ### initiate dfs for all neighbours of the board and then bool (True) will propogate backwards
        def dfs(r,c,i):
            if i==length:
                return True
            if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or (r,c) in path):
                return False

            path.add((r,c))

            res=(dfs(r+1,c,i+1) or 
                dfs(r,c+1,i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c-1,i+1))

            path.remove((r,c)) ## cleaning the path going back
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True

        return False                


            



        