from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Create a binary tree to traverse through it in an inorder traversal manner
#
#         Root    2
#              /     \
#             2        5  
#            / \      /  \
#           1   3    5    7

#
root = TreeNode(2)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def levelOrderTraversal(self, root):
        levelOrderTraversedList = []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                levelOrderTraversedList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return levelOrderTraversedList

solution = Solution()
pre_invert_tree = solution.levelOrderTraversal(root)
response = solution.invertTree(root)
post_invert_tree = solution.levelOrderTraversal(response)
print(f'The Level-Order traversed list of the given tree is {pre_invert_tree}')
print(f'The Level-Order traversed list of inverted tree is {post_invert_tree}')