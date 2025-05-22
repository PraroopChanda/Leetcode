# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        qu=deque([root])
        output=[]
        while qu:
            list1=[]
            for x in range(len(qu)):
               curr=qu.popleft()
               list1.append(curr.val)
               if curr.left:
                qu.append(curr.left)
               if curr.right:
                qu.append(curr.right)
            output.append(list1)
        return output         

        