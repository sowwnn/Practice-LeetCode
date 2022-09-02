# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)
        
    def dfs(self,node):
        if not node:
            return 
        
        self.dfs(node.left)
        self.dfs(node.right)
        
        node.left, node.right = node.right, node.left
        return node
