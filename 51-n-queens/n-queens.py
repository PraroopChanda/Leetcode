class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        states=[]
        ## initially solving assuming state to be given as (r,c) matrix

        ## validity check
        def is_valid(states):
            return len(states)==n
            

        ## for each next row i want to get all possible solutions
        def get_candidates(states):
            candidates=[]
            row=len(states) ## this is the row that we are searching now
            cols=range(n)
            for col in cols:
                flag=True
                for r,c in states:
                    if c==col: ## column check for queens
                        flag=False
                        break
                    if abs(r-row)==abs(c-col): ## shouldn't be in the same diagnol
                        flag=False
                        break
                if flag:        
                    candidates.append((row,col))

            return candidates

        ## now defining our recursive search

        def search(states):
            if is_valid(states):
                #result.append(states.copy()) 
                board=[]
                for r,c in states:
                    row=['.']*n
                    row[c]='Q'
                    board.append("".join(row))
                result.append(board)

            for cand in get_candidates(states):
                states.append(cand)
                search(states)
                states.pop()

        search(states)

        return result              



        