# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.bfs(root)
        return self.res
        
    def bfs(self,root):
        if not root:
            return 0
        else:
            left = self.bfs(root.left)
            right = self.bfs(root.right)
            self.res = max(self.res, left+right)
            return 1 + max(left,right)
    
         
