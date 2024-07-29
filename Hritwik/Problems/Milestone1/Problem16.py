# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []
        queue = deque([root])
        response = []
        while queue:
            len_of_queue = len(queue)
            sum=0
            level = []
            for i in range(len_of_queue):
                node = queue.popleft()
                level.append(node.val)
                sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg_of_level = sum/len_of_queue
            response.append(avg_of_level)
        return response


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


response = solution.averageOfLevels(root)
print(f'The average value of the nodes on each level in the form of an array. -> {response}')
