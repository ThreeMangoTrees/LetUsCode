class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Create a binary tree to traverse through it in an inorder traversal manner
#
#         Root    12
#              /     \
#             8        4  
root = TreeNode(12)
root.left = TreeNode(8)
root.right = TreeNode(4)

class Solution:
    def checkTree(self, root) -> bool:
        return root.val==root.left.val+root.right.val
    
solution = Solution()
response = solution.checkTree(root)
print(f'Value of the root is equal to the sum of the values of its two children. [True/False]: {response}')
