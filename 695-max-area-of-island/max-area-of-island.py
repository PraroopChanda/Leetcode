class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        row_len=len(grid)
        col_len=len(grid[0])
        def dfs(r,c,area):
            if r<0 or r>=row_len or c<0 or c>=col_len:
                return area
            if grid[r][c]==0:
                return area
            grid[r][c]=0
            area+=1

            area=dfs(r-1,c,area)
            area=dfs(r+1,c,area)
            area=dfs(r,c-1,area)
            area=dfs(r,c+1,area)

            return area

        for r in range(row_len):
            for c in range(col_len):
                area=0
                area=dfs(r,c,area)
                if area>max_area:
                    max_area=area

        return max_area            
                            
        


        