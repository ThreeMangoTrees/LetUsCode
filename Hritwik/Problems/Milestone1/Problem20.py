from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:       
    def rangeSumBST(self, root, low: int, high: int) -> int:
        if root is None:
            return 0
        queue = deque([root])
        sum = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.val>=low and node.val<=high:
                    sum+=node.val
        return sum

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

low, high = 3, 6
response = solution.rangeSumBST(root, low, high)
print(f'The sum of values of all nodes with a value in the inclusive range [low, high] is {response}')
