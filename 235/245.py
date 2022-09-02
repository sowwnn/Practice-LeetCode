# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        
        return self.find(root)
        
        
    def find(self, root):
        if (root == self.p or root == self.q or not root): return root 

  
        left = self.find(root.left)
        right = self.find(root.right) 

        if left and right: return root 
        elif left: return left
        elif right: return right
