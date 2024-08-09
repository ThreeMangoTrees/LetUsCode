from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Traverse on the cloned tree to get the target node and return that node
        queue=deque([cloned])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if target.val == node.val:
                    return node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

# Create Original binary tree to traverse through it in an inorder traversal manner
#
#     Original    2
#              /     \
#             8        5  
#            / \        \
#           1   3        7

original = TreeNode(2)
original.left = TreeNode(8)
original.left.left = TreeNode(1)
original.left.right = TreeNode(3)
original.right = TreeNode(5)
original.right.right = TreeNode(7)
# Create a cloned tree to traverse through it in an inorder traversal manner
#
#        Cloned   2
#              /     \
#             8        5  
#            / \        \
#           1   3        7
cloned = TreeNode(2)
cloned.left = TreeNode(8)
cloned.left.left = TreeNode(1)
cloned.left.right = TreeNode(3)
cloned.right = TreeNode(5)
cloned.right.right = TreeNode(7)

solution = Solution()
target = TreeNode(8)
response = solution.getTargetCopy(original, cloned, target)
print(f'Value of the reference to the target node in the cloned tree.: {response.val}')
