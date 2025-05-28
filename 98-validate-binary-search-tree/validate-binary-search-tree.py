# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def valid(node,left,right):
            if node is None:
                return True
            if not(node.val>left and node.val<right):
                return False
            return valid(node.left,left,node.val) and valid(node.right,node.val,right)

        return valid(root,-inf,inf)                
        