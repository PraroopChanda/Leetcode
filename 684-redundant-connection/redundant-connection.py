class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=list(range(n+1))
        rank=[1]*(n+1)

        def find(x): ## basically find its parent
            if x==parent[x]:
                print("after getting inside parent",x)
                return parent[x]
            else:
                print("this is the parent",parent[x])
                return find(parent[x])

        def union(a,b): ## the logic of how to combine 2 nodes/edges
            pa,pb =find(a),find(b)
            print(pa,pb)
            if pa==pb: ## meaning there already exists a connection between the two
                return False
            ## now compare their rank to decide parent and child relationship
            if rank[pa]<rank[pb]:
                parent[pa]=pb
            elif rank[pa]>rank[pb]:
                parent[pb]=pa
            else:
                parent[pb]=pa
                print("parent changed to",parent)
                rank[pa]+=rank[pb]
            return True         

        for u,v in edges:
            if not union(u,v):
                return [u,v]






        # output=[]
        # visited=set()
        # premap={x:[] for x in range(1,len(edges)+1)}
        # for r,c in edges:
        #     premap[r].append(c)
        # def dfs(node,parent):
        #     if node in visited:
        #         output.append([parent,node])
        #         return

        #     visited.add(node)
        #     for nei in premap[node]:
        #         dfs(nei,node)

        #     return

        # node=next(iter(premap))
        # print(node)
        # dfs(node,-1)

        # print(output)
        # if len(output)==1:
        #     return output[0]
        # else:
        #     return output[-1]    
            
        