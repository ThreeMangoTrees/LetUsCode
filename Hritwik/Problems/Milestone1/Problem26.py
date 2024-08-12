class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Create a binary tree to traverse through it in an inorder traversal manner
#
#     Root1  3                    Root2  2       
#          /    \                       / \                     
#         1      2                     9   3                  
#               /  \                               
#              9    3                        

root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(3)

root2 = TreeNode(2)
root2.left = TreeNode(9)
root2.right = TreeNode(3)

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
    def isSameTree(self,node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val!=node2.val:
            return False
        
        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)
   
solution = Solution()
response = solution.isSubtree(root1, root2)
print(f'There is a subtree of root with the same structure and node values of subRoot [True or False]: {response}')
