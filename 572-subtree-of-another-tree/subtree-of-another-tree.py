# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue=deque([root])
        subquque=deque([subRoot])
        answer=False
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)                   
        while queue:
            curr=queue.popleft()
            if curr.val==subRoot.val:
                answer=isSameTree(curr,subquque.popleft())
                if answer==True:
                    break
                subquque=deque([subRoot])    
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return answer         