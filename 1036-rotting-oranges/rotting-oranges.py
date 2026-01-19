class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row_len=len(grid)
        col_len=len(grid[0])
        visited=set()
        queue=deque()
        total_time=0

        def addqueue(r,c):
            if r<0 or r>=row_len or c<0 or c>=col_len or (r,c) in visited or grid[r][c]==0:
                return 
            queue.append((r,c))
            visited.add((r,c))    

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c]==2:
                    queue.append((r,c))
                    visited.add((r,c))

        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                grid[r][c]=2

                addqueue(r+1,c)
                addqueue(r-1,c)
                addqueue(r,c-1)
                addqueue(r,c+1)
            total_time+=1
            if len(queue)==0:
                total_time-=1

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c]==1:
                    return -1  
        return total_time 


        # from collections import deque
        # row_len=len(grid)
        # col_len=len(grid[0])
        # visited=set()
        # queue=deque()
        # total_time=0

        # def addqueue(r,c):
        #     if r<0 or r>=row_len or c<0 or c>=col_len or (r,c) in visited or grid[r][c]==0:
        #         return 
        #     queue.append((r,c))
        #     visited.add((r,c))    

        # for r in range(row_len):
        #     for c in range(col_len):
        #         if grid[r][c]==2:
        #             queue.append((r,c))
        #             visited.add((r,c))

        # while queue:
        #     for i in range(len(queue)):
        #         r,c=queue.popleft()
        #         grid[r][c]=2

        #         addqueue(r+1,c)
        #         addqueue(r-1,c)
        #         addqueue(r,c-1)
        #         addqueue(r,c+1)
        #     total_time+=1

        # for r in range(row_len):
        #     for c in range(col_len):
        #         if grid[r][c]==1:
        #             return -1  
        # return total_time-1    


        
        