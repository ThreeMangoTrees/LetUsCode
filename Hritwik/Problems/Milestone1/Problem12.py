# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.response = TreeNode(-1)

    def searchBST(self, root, val: int) -> TreeNode:
        if root is None:
            return None
        
        if root.val == val:
            self.response = root
            return root

        if root.val>val:
            self.searchBST(root.left, val)
        
        if root.val<val:
            self.searchBST(root.right, val)

        return self.response if self.response.val != -1 else None
    
    def inorderTraversal(self, root: None):
        self.response=[]
    
        def traverse(node):
            if node is None:         
                return None            
            traverse(node.left)
            self.response.append(node.val)
            traverse(node.right)

        traverse(root)
        return self.response    

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

value_to_search = 20
response_root = solution.searchBST(root, value_to_search )
final_response = solution.inorderTraversal(response_root)
print(f'The subtree rooted with node (with value equal to {value_to_search}): {final_response}')

    

