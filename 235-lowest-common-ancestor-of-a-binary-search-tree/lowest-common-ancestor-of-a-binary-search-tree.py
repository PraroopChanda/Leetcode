# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        level_dict={}
        qu=deque([(root,1)])# 1 is the depth here
        level=1
        parent_dict={root.val:None}
        while qu:
            if p.val in level_dict and q.val in level_dict:
                break
            for x in range(len(qu)):
                curr,depth=qu.popleft()
                level_dict[curr.val]=depth
                if curr.left:
                    qu.append((curr.left,depth+1))
                    parent_dict[curr.left.val] = curr
                if curr.right:
                    qu.append((curr.right, depth+1))   
                    parent_dict[curr.right.val] = curr

        # 2. Create set of all ancestors of p
        ancestors = set()
        while p:
            print(p.val)
            ancestors.add(p.val)
            p = parent_dict[p.val] ## travers upward the tree level by level
            

        # 3. Traverse q's ancestry, return the first match
        while q:
            if q.val in ancestors:
                return q  # this TreeNode is the LCA
            q = parent_dict[q.val]

        print(level_dict)            
                    

            

        