# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create a binary tree to traverse through it in an inorder traversal manner
#
#         Root   3
#              /    \
#             9      20  
#                   /  \
#                  15   7
#
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        leftHasTargetSum = self.hasPathSum(root.left, targetSum-root.val)
        rightHasTargetSum = self.hasPathSum(root.right, targetSum-root.val)

        if leftHasTargetSum or rightHasTargetSum:
            return True
        else:
            return False

solution = Solution()
target = 30
response = solution.hasPathSum(root,target)
print(f'The tree has a root-to-leaf path such that adding up all the values along the path equals targetSum : {response}')     
