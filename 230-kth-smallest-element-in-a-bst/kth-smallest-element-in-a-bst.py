# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result=None
        self.count=0

        def inorder_traversal(node):
            if node is None or self.result is not None:
                return 
            inorder_traversal(node.left) ## in the end this would be the smallest node (till it goes recursively)
            ## at the end of the tree
            
            self.count+=1 ## when invoked for the first time this is the smallest element
            ## this is kind of taking the value upwards in the chain
            ## like counting the total number of nodes

            if self.count==k:
                self.result=node.val
            inorder_traversal(node.right)
            return self.result 

        return inorder_traversal(root)    

        