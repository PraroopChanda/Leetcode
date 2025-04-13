class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map={x:set() for x in range(len(board))}
        col_map={x:set() for x in range(len(board[0]))}
        box_map={(x,y):set() for y in range(3) for x in range(3)}

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]==".":
                    continue
                if board[x][y] in row_map[x] or board[x][y] in col_map[y] or board[x][y] in box_map[(x//3,y//3)]:
                    return False
                else:
                    row_map[x].add(board[x][y])
                    col_map[y].add(board[x][y])
                    box_map[(x//3,y//3)].add(board[x][y])
        return True                


