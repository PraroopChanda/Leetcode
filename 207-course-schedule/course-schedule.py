class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## first creating a hash set 
        premap={x:[] for x in range(numCourses)}

        for r,c in prerequisites:    
            premap[r].append(c)
        
        print(premap)
        visited=set()

        def dfs(r):
            for nei in premap[r]:
                if nei in visited: 
                    return False
                visited.add(nei)
                if not dfs(nei): 
                    return False
                visited.remove(nei)
                premap[r].remove(nei)   

            return True

        for r in range(numCourses):
            if not dfs(r):
                return False
        return True        
                    
