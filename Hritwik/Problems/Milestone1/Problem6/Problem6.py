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
    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    
solution = Solution()
response = solution.maxDepth(root)
print(f'Max Depyth of the tree : {response}')


        