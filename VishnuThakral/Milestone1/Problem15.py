# Milestone1 Problem 15 - Leetcode 110(Balanced Binary Tree: https://leetcode.com/problems/balanced-binary-tree/description/)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return -1
            else:
                return 1 + max(height(node.left), height(node.right))

        if not root:
            return True
        else:
            return abs(height(root.left) - height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(
                root.right)