# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0

        def dfs(curr):
            if curr is None:
                return 0
            left=dfs(curr.left)
            right=dfs(curr.right) 

            self.res=max(self.res,left+right) ## left + right is the diameter actually
            ## basically in a recursive way i check for each node, whether its left+right is greater or less than other nodes (diameters)

            return 1+ max(left,right) ## this will output the height ( This is normal getting the depth of the tree)

        dfs(root)
        return self.res




        
    #     if not root:
    #         return 0
    #     ## basically counting the edges
    #     left_height=self.maxheight(root.left)
    #     right_height=self.maxheight(root.right)
    #     diameter=left_height+right_height
    #     sub=max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)) ## this is now again checking for each node
    #     return max(diameter,sub)

    # def maxheight(self,root: Optional[TreeNode])-> int:
    #     if not root:
    #         return 0
    #     return 1+max(self.maxheight(root.left),self.maxheight(root.right))        