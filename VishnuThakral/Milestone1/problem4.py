# Leetcode Problem number 100 (https://leetcode.com/problems/same-tree/description/)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if p is None and q is None:
                return True
            elif p is None and q is not None:
                return False
            elif p is not None and q is None:
                return False
            if p.val == q.val:
                return check(p.left, q.left) and check(p.right, q.right)

        return check(p, q)

