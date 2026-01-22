class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=list(range(n+1))
        rank=[1]*(n+1)

        def find(x): ## basically find its parent
            if x==parent[x]:
                return parent[x]
            else:
                return find(parent[x])

        def union(a,b): ## the logic of how to combine 2 nodes/edges
            pa,pb =find(a),find(b)
            if pa==pb: ## meaning there already exists a connection between the two
                return False
            ## now compare their rank to decide parent and child relationship
            if rank[pa]<rank[pb]:
                parent[pa]=pb
            elif rank[pa]>rank[pb]:
                parent[pb]=pa
            else:
                parent[pb]=pa
                rank[pa]+=rank[pb]
            return True         

        for u,v in edges:
            if not union(u,v):
                return [u,v]