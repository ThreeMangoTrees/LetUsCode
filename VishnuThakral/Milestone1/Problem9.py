#Milestone 1 Problem 9: leetcode Problem No. 113 (https://leetcode.com/problems/path-sum-ii/description/)
# Time: O(N), Space O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_paths(self, node,p_list, p_sum, target):
        if node:
            p_sum = p_sum + node.val
            p_list = p_list + [node.val]
            if p_sum == target and not node.left and not node.right:
                self.res.append(p_list)
                return 0
            if node.left:
                self.find_paths(node.left,p_list, p_sum, target)
            if node.right:
                self.find_paths(node.right, p_list, p_sum, target)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.find_paths(root, [], 0, targetSum)
        return self.res