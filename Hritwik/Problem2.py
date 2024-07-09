class Node:
    """
    A class to represent a node in a binary search tree.
    
    Attributes:
    ----------
    value : int
        The value stored in the node.
    left : Node or None
        The left child of the node.
    right : Node or None
        The right child of the node.
    """
    def __init__(self, value: int):
        self.value=value
        self.left=None
        self.right=None

# Create a binary tree to traverse through it in an inorder traversal manner
#
#         Root   1
#              /    \
#             2      3  
#            / \    /  \
#           4   5  6    7
#          /
#         8
#
root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left= Node(8)

# Inorder traversal of the above binary tree

class Solution:

    def __init__(self):
        # Initializes Solution object
        pass
    
    def preorderTraversal(self, root: None):
        self.response=[]
    
        def traverse(node):
            if node is None:         
                return None  
            self.response.append(node.value)          
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.response

    def postorderTraversal(self, root: None):
        self.response=[]
    
        def traverse(node):
            if node is None:         
                return None       
            traverse(node.left)
            traverse(node.right)
            self.response.append(node.value)     

        traverse(root)
        return self.response

    

solution = Solution()

preorder_traversed_list = solution.preorderTraversal(root)
print(f'preorder traversed list : {preorder_traversed_list}')

postorder_traversed_list = solution.postorderTraversal(root)
print(f'postorder traversed list : {postorder_traversed_list}')






