# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def getMinimumDifference(self, root) -> int:
        queue = deque([root])
        min_diff_list = []
        elements = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                elements.append(node.val)
                if node.left:
                    queue.append(node.left)         
                if node.right:
                    queue.append(node.right)
        elements = sorted(elements)
        min_diff = float('inf')
        for i in range(len(elements)-1):
            min_diff = min (min_diff, abs(elements[i]-elements[i+1]))
        return min_diff
    
solution = Solution()

# Create a binary tree to traverse through it in an inorder traversal manner
#
#         Root   2
#              /    \
#             1      5  
#                   /  \
#                  4    7
#
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(7)


response = solution.getMinimumDifference(root)
print(f'the minimum absolute difference between the values of any two different nodes in the tree. -> {response}')

