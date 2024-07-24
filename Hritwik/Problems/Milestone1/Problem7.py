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
    def __init__(self):
        self.sum=0

    def sumOfLeftLeaves_(self, node):
        if node is None:
            return 0
        if node.left and node.left.left is None and node.left.right is None:    
            self.sum += node.left.val
        self.sumOfLeftLeaves_(node.left)
        self.sumOfLeftLeaves_(node.right)
        return self.sum
        
    def sumOfLeftLeaves(self, root) -> int:
        response = self.sumOfLeftLeaves_(root)
        return response

solution = Solution()
response = solution.sumOfLeftLeaves(root)
print(f'Sum of Left Leaves is : {response}')


        