# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkTree(self,root:Optional[TreeNode],subRoot:Optional[TreeNode]):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        if root.val != subRoot.val:
            return False

        left = self.checkTree(root.left,subRoot.left)
        right = self.checkTree(root.right,subRoot.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def dfs(root,subRoot):
            nonlocal res
            if not root :
                return

            if self.checkTree(root,subRoot):
                res = True
                return
            else:
                dfs(root.left,subRoot)
                dfs(root.right,subRoot)

        dfs(root,subRoot)
        return res