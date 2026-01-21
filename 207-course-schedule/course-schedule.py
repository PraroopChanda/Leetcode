class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## first creating a hash set 
        premap={x:[] for x in range(numCourses)}

        for r,c in prerequisites:    
            premap[r].append(c)
        visited=set()

        def dfs(r):
            if r in visited:  ## base case for detecting cycles
                return False
            visited.add(r)    
            for nei in premap[r]:
                if not dfs(nei): 
                    return False
            visited.remove(r)
            premap[r]=[]  
            return True

        for r in range(numCourses):
            if not dfs(r):
                return False
        return True        
                    
