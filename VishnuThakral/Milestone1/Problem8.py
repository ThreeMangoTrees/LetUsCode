#Milestone1/Problem8 - Leetcode no. 112(https://leetcode.com/problems/path-sum/)
#Time: O(N), Space O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def find_path(node, present, target):
            if node:
                present += node.val
                if not node.left and not node.right:
                    if present == target:
                        return True
                    return False

                return find_path(node.left, present, target) or find_path(node.right, present, target)
            return False

        if not root:
            return False
        return find_path(root, 0, targetSum)