# Milestone1 Problem 13: Leetcode 671 (https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/)
# Selective Level Order Traversal
# Time:O(N), Space: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res = math.inf
        level = 1
        stack = [root]
        flag=False
        while stack:
            p = stack.pop()
            if p:
                if p.val == root.val:
                    stack.append(p.left)
                    stack.append(p.right)
                if p.val <= res and p.val>root.val:
                    res = p.val
                    flag=True
        if flag:
            return res
        return -1
