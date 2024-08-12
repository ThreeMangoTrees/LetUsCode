# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def pathSum(self, root, targetSum):
        response = []
        queue = []
        def solve(node, target):
            if node is None:
                return      
            queue.append(node.val)
            if not node.left and not node.right and node.val==target:
                response.append(list(queue))
            solve(node.left, target-node.val)
            solve(node.right, target-node.val)
            queue.pop()
        solve(root, targetSum)    
        return response

# Create a binary tree to traverse through it in an inorder traversal manner
#
#         Root   3
#              /    \
#             9      20  
#                   /  \
#                  15   7
#
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)  

targetSum = 38
solution = Solution()
response = solution.pathSum(root,targetSum)
print(f'All root-to-leaf paths where the sum of the node values in the path equals targetSum : {response}')
