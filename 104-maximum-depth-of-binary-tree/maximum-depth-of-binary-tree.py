# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## solving by BFS level by level
        level=0
        if root is None:
            return 0
        queue=deque([root])
        while queue:
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level+=1        
        return level
        ## solving by DFS first using a stack 
        # stack= [(root,1)] ## 1 is the depth
        # res=0 ## final depth
        # while stack:
        #     curr,depth=stack.pop()
        #     if curr:
        #         res=max(depth,res)
        #         stack.append((curr.left,depth+1))
        #         stack.append((curr.right,depth+1))

        # return res    
