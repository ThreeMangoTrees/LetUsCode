# Definition for a binary tree node.
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
            self.capacity = 0
            def height(node):
                if node is None:
                    return 0
                leftHeight = height(node.left)
                rightHeight = height(node.right)
                self.capacity = max(self.capacity, leftHeight+rightHeight)
                return 1+max(leftHeight, rightHeight)
            height(root)
            return self.capacity
    
solution = Solution()

# Create a binary tree to traverse through it in an inorder traversal manner
#
#         Root   2
#              /    \
#             2      5  
#                   /  \
#                  5    7
#
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)


response = solution.diameterOfBinaryTree(root)
print(f'The length of the diameter of the tree is {response}')
