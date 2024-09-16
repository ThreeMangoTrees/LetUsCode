#Milestone 1: Problem 7 - Leetcode 404 (https://leetcode.com/problems/sum-of-left-leaves/description/)
#Time Complexity: O(N), Space: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_sum(self, node, flag):
        if flag==True and not node.left and not node.right:
            self.res+=node.val
        if node.left:
            self.get_sum(node.left, True)
        if node.right:
            self.get_sum(node.right, False)
        return 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.get_sum(root, False)
        return self.res