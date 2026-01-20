class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_len=len(heights)
        col_len=len(heights[0])
        pac_set=set()
        at_set=set()
        pac_visited=set()
        at_visited=set()
        output=[]

        def dfs(r,c,r_1,c_1):
            if r<0 or r>=row_len or c<0 or c>=col_len or (r,c) in pac_visited or heights[r][c]<heights[r_1][c_1] :
                return
            pac_set.add((r,c))
            pac_visited.add((r,c))

            dfs(r+1,c,r,c)
            dfs(r-1,c,r,c)
            dfs(r,c-1,r,c)
            dfs(r,c+1,r,c)

        def dfs_at(r,c,r_1,c_1):
            if r<0 or r>=row_len or c<0 or c>=col_len or (r,c) in at_visited or heights[r][c]<heights[r_1][c_1] :
                return
            at_set.add((r,c))
            at_visited.add((r,c))

            dfs_at(r+1,c,r,c)
            dfs_at(r-1,c,r,c)
            dfs_at(r,c-1,r,c)
            dfs_at(r,c+1,r,c)

        for c in range(col_len):
            dfs(0,c,0,c)
        for r in range(row_len):
            dfs(r,0,r,0)
        for r in range(row_len):
            dfs_at(r,col_len-1,r,col_len-1)     
        for c in range(col_len):
            dfs_at(row_len-1,c,row_len-1,c)

        for r in range(row_len):
            for c in range(col_len):
                if (r,c) in pac_set and (r,c) in at_set:
                    output.append([r,c])

        return output            
                                       

