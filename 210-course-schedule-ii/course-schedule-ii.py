class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output=[]
        premap={x:[] for x in range(numCourses)}

        for r,c in prerequisites:
            premap[r].append(c)    
        visited=set()

        def dfs(cr):
            if cr in visited:
                return False
            if cr in output:
                return True 
            visited.add(cr)      
            for nei in premap[cr]:
                if not dfs(nei):
                    return False
            visited.remove(cr)        
            output.append(cr)
            return True

        for x in range(numCourses):
            if not dfs(x):
                return []
        return output        
                



        