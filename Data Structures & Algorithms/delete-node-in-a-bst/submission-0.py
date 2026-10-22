# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delete(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        # Find the smallest node in the right subtree
        successor = root.right

        while successor.left:
            successor = successor.left

        # Replace root's value
        root.val = successor.val

        # Delete the original successor
        parent = root
        curr = root.right

        while curr.val != successor.val:
            parent = curr
            curr = curr.left

        # Successor has no left child
        if parent.left == curr:
            parent.left = curr.right
        else:
            parent.right = curr.right

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.val == key:
            return self.delete(root)
        
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        
        return root