#Milestone 1 Problem 12: Search in BST, Leetcode number 700(https://leetcode.com/problems/search-in-a-binary-search-tree/description/)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val==val:
                return root
            elif root.val>val:
                return self.searchBST(root.left,val)
            elif root.val<val:
                return self.searchBST(root.right,val)
        return None