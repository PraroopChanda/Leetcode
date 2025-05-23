# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        output=[]
        qu=deque([root])
        while qu:
            y=len(qu)-1
            for x in range(len(qu)):
                curr=qu.popleft()
                if x==y:
                    output.append(curr.val)
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
        return output                    