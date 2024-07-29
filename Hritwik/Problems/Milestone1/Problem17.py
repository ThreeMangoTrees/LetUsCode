# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   

    def findMode(self, root): 
        if not root:
            return []
        hash_map = {}
        queue = deque([root])
        while queue:
            level = []
            len_of_queue = len(queue)
            for _ in range(len_of_queue):
                node = queue.popleft()
                if node.val in hash_map:
                    hash_map[node.val]+=1
                else:
                    hash_map[node.val]=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        max_value = max(hash_map.values())
        mode_keys = [key for key, value in hash_map.items() if value == max_value]
               
        return mode_keys

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


response = solution.findMode(root)
print(f'The mode(s) of the BST with the given root is/are. -> {response}')

