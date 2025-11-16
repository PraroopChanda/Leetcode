class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # result=[]
        # states=[]
        # ## initially solving assuming state to be given as (r,c) matrix

        # ## validity check
        # def is_valid(states):
        #     return len(states)==n

        # ## for each next row i want to get all possible solutions
        # def get_candidates(states):
        #     candidates=[]
        #     row=len(states) ## this is the row that we are searching now
        #     cols=range(n)
        #     for col in cols:
        #         flag=True
        #         for r,c in states:
        #             if c==col: ## column check for queens
        #                 flag=False
        #                 break
        #             if abs(r-row)==abs(c-col): ## shouldn't be in the same diagnol
        #                 flag=False
        #                 break
        #         if flag:        
        #             candidates.append((row,col))

        #     return candidates

        # ## now defining our recursive search

        # def search(states):
        #     if is_valid(states):
        #         #result.append(states.copy()) 
        #         board=[]
        #         for r,c in states:
        #             row=['.']*n
        #             row[c]='Q'
        #             board.append("".join(row))
        #         result.append(board)

        #     for cand in get_candidates(states):
        #         states.append(cand)
        #         search(states)
        #         states.pop()

        # search(states)

        # return result              

        ## assuming map stored in 1D array and not 2d
        result=[]
        states=[]

        def is_valid(states):
            return (len(states)==n)

        def get_candidates(states): ## basically for each next row we search for possible states ( we only need to search for one next row thats it)
            if not states:
                return list(range(n))
            row=len(states) ## next row to search
            cols=range(n) ## columns to search for
            candidates=[]

            for col in cols:
                flag=True
                for r,c in enumerate(states):
                    if c==col: ## checking for columns
                        flag=False
                        break
                    if abs(row-r)==abs(col-c): ## basically diagnol check and difference in row, col from one point should be same to be diagnol
                        flag=False
                        break
                if flag:
                    candidates.append(col)
            return candidates        

        def search(states): ## our main recursive functions ---> start with all pairs and the come back and recurse
            if is_valid(states):
                board=[]
                for (col) in states:
                    row=["."]*n
                    row[col]='Q'
                    board.append("".join(row))
                result.append(board)

            for cand in get_candidates(states):
                states.append(cand)
                search(states)
                states.pop()

        search(states)
        return result           