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
#             8        5  
#            / \        \
#           1   3        7
root = TreeNode(2)
root.left = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(5)
root.right.right = TreeNode(7)

class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:        
        queue = deque([(root, None, 0)])
        x_info, y_info = None, None
        while queue:
            for _ in range(len(queue)):
                node, parent, depth = queue.popleft()
                if node.val==x:
                    x_info = (parent, depth)
                if node.val == y:
                    y_info = (parent, depth)
                
                if node.left:
                    queue.append((node.left, node, depth+1))
        
                if node.right:
                    queue.append((node.right, node, depth+1))
                
                if x_info and y_info:
                    break
        
        if x_info[0] != y_info[0] and x_info[1] == y_info[1]:
            return True
        else:
            return False
        
solution = Solution()
x, y = 1, 7
response = solution.isCousins(root, x, y)
print(f'values {x} and {y} in the tree are cousins [True/False]: {response}')
