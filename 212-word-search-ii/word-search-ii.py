class trienode:
    def __init__(self):
        self.children={}
        self.endofWord=False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=trienode()
        row_len=len(board)
        col_len=len(board[0])
        for word in words:
            current=root
            for w in word:
                if w not in current.children:
                    current.children[w]=trienode()
                current=current.children[w]
            current.endofWord=True

        visited=set()
        output=set()
        def dfs(row,col,node,word):
            if (row<0 or row>=row_len or col<0 or col>=col_len or  (row,col) in visited or board[row][col] not in node.children):
                return
            visited.add((row,col))  
            node=node.children[board[row][col]]
            word+=board[row][col]  

            if node.endofWord:
                output.add(word)

            dfs(row-1,col,node,word)    
            dfs(row+1,col,node,word)    
            dfs(row,col+1,node,word)    
            dfs(row,col-1,node,word)

            visited.remove((row,col)) ## so that i can see other words as well 

        ##word tree creation done
        for row in range(row_len):
            for col in range(col_len):
                word=""
                dfs(row,col,root,word)

        return list(output)        
                    
        