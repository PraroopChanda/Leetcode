# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        self.result=root.val
        ## going for postorder traversal
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            leftmax=max(0,left) ## basically doing this for negative values
            rightmax=max(0,right)

            self.result=max(self.result,node.val+leftmax+rightmax)
            return (node.val+max(leftmax,rightmax))

        dfs(root)
        return self.result        
        
        

        