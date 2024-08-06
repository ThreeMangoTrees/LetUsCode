from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Create a binary tree to traverse through it in an inorder traversal manner
#
#     Root1  3                    Root2  2         # Response     5
#          /    \                       / \                      / \
#         1      20                    9   3                   10   23
#                 \                   /   /                   /     /\
#                  7                 7   2                   7     2  7

root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(20)
root1.right.right = TreeNode(7)

root2 = TreeNode(2)
root2.left = TreeNode(9)
root2.right = TreeNode(3)
root2.left.left = TreeNode(7)
root2.right.left = TreeNode(2)

class Solution:
    def __init__(self):
        self.response = TreeNode()
    def mergeTrees(self, root1, root2):
        if not root1:
            if not root2:
                return None
            else:
                return root2
        if not root2:
            if not root1:
                return None
            else:
                return root1
        response = TreeNode(root1.val+root2.val)
        response.left = self.mergeTrees(root1.left, root2.left)
        response.right = self.mergeTrees(root1.right, root2.right)
        return response
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
response_tree = solution.mergeTrees(root1, root2)
level_order_traversed_tree = solution.levelOrder(response_tree)
print(f'Merged tree of Binary trees with root-  Root1 and Root2 is : {level_order_traversed_tree}')
