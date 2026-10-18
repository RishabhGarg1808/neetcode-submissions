# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travelPreorder(self, root: Optional[TreeNode], res:List[int]):
        if root is None:
            return
        
        res.append(root.val)
        self.travelPreorder(root.left,res)
        self.travelPreorder(root.right,res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        self.travelPreorder(root,res)

        return res    