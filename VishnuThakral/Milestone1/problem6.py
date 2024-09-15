#Problem 6: Leetcode Question No. 104 (https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def iterate(node, count):
            if not node:
                return count
            count+=1
            return max(iterate(node.left,count), iterate(node.right,count))

        count = 0
        return iterate(root,count)