# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_dict={root.val:None}
        qu=deque([root])
        while qu:
            if p.val in parent_dict and q.val in parent_dict:
                break
            for x in range(len(qu)):
                curr=qu.popleft()
                if curr.left:
                    qu.append(curr.left)
                    parent_dict[curr.left.val]=curr ## storing the parent information
                if curr.right:
                    qu.append(curr.right)
                    parent_dict[curr.right.val]=curr
        ## traversing up the chain
        ancestor=set()
        while p:
            ancestor.add(p.val)
            p=parent_dict[p.val] ## basically traversing up the graph

        while q:
            if q.val in ancestor:
                return q
            q=parent_dict[q.val]    


                


                    

            

        