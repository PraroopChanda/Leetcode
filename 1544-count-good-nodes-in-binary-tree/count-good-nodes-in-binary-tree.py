# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return None
        max_val=root.val
        self.output=0
        ## solving with dfs
        def dfsgood(node,max_val):
            if not node:
                return 
            if node.val>=max_val:
                self.output+=1
            max_val=max(node.val,max_val)
            left=dfsgood(node.left,max_val)
            right=dfsgood(node.right,max_val)

        dfsgood(root,max_val)
        return self.output         
        