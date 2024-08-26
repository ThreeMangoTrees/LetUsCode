# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        # Get the middle element of the sorted element to divide the array into two parts
        new_node=TreeNode(nums[len(nums)//2]) 
        new_node.left=self.sortedArrayToBST(nums[:len(nums)//2])
        new_node.right=self.sortedArrayToBST(nums[len(nums)//2+1:])
        return new_node

solution = Solution()
nums = [-10,-3,0,5,9]
response = solution.sortedArrayToBST(nums)

