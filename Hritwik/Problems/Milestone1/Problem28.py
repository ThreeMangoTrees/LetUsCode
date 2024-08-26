class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        response = []
        def inorder_(node):
            if node is None:
                return
            if node.left:
                inorder_(node.left)
            response.append(node.val)
            if node.right:
                inorder_(node.right)
        inorder_(root)
        response_head=TreeNode(-1,None)
        response_iter = response_head
        for node in response:
            tree_node = TreeNode(node, None)
            response_iter.right = tree_node
            response_iter = response_iter.right
        return response_head.right
    
# Create Original binary tree to traverse through it in an inorder traversal manner
#
#     Original    4
#              /     \
#             3        5  
#            / \        \
#           1   2        7

original = TreeNode(4)
original.left = TreeNode(3)
original.left.left = TreeNode(1)
original.left.right = TreeNode(2)
original.right = TreeNode(5)
original.right.right = TreeNode(7)

solution = Solution()
response = solution.increasingBST(original)
print(f'Response root.: {response}')
