# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        
        queue = [root]
        response = []

        while queue:
            level=[]
            for i in range(len(queue)):
                top_of_queue = queue.pop(0)
                level.append(top_of_queue.val)
                if top_of_queue.left:
                    queue.append(top_of_queue.left) 
                if top_of_queue.right:
                    queue.append(top_of_queue.right)               
            response.append(level)
        return response
    
        
solution = Solution()

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

response = solution.levelOrder(root)
print(f'List of nodes in each Level : {response}')

    

