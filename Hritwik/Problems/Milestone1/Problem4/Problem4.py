# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Create a binary tree to traverse through it in an inorder traversal manner
#
#         Root1  3
#              /    \
#             9      20  
#                   /  \
#                  15   7
#
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

# Create another binary tree to traverse through it in an inorder traversal manner
#
#         Root2  3
#              /    \
#             9      20  
#                   /  \
#                  15   7
#
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

class Solution:
    def isSameTree(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        
        elif not root1 or not root2:
            return False
        
        elif root1.val != root2.val:
            return False
        
        else:
            return self.isSameTree(root1.left,root2.left) and self.isSameTree(root1.right,root2.right)
        
solution = Solution()
response = solution.isSameTree(root1, root2)
print(f'Binary trees with root-  Root1 and Root2 are same [True or False] ? : {response}')

        
