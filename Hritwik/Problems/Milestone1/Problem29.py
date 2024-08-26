from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root) -> bool:
        UnivValue = root.val
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val != UnivValue:
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return True
# Create Original binary tree to traverse through it in an inorder traversal manner
#
#     root        1
#              /     \
#             1        1  
#            / \        \
#           1   1        1

root = TreeNode(1)
root.left = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.right = TreeNode(1)

solution = Solution()
response = solution.isUnivalTree(root)
print(f'The tree with the given root is Universal Tree. [True/False].: {response}')