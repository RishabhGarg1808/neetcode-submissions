# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth (self,root : Optional[TreeNode]):
        if root is  None:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)

        return 1 + max(left,right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)

