# Definition for a binary tree node.
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isBalanced(self, root) -> bool:
        # method to get height recursively
        def getHeight(node):
            if node is None:
                return 0
            
            left_tree_height = getHeight(node.left)
            if left_tree_height == -1:
                return -1
            
            right_tree_height = getHeight(node.right)
            if right_tree_height == -1:
                return -1
            
            if abs(left_tree_height-right_tree_height)>1:
                return -1
            
            return max(left_tree_height, right_tree_height)+1
            
        response = getHeight(root)
        if response == -1:
            return False
        else:
            return True
        

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


response = solution.isBalanced(root)
print(f'The tree with the given root is height-balanced. -> {response}')

