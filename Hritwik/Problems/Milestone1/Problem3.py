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

class Solution:
    def __init__(self):
        self.root = None
        pass
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_(self.root, key)

    def insert_(self, node, key):
        if node.value > key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_(node.right, key)
    
    def inorderTraversal(self):
        self.response=[]
        self.inorderTraversal_(self.root)
        return self.response
        
    def inorderTraversal_(self, root):
        def traverse(node):
            if node is None:         
                return None            
            traverse(node.left)
            self.response.append(node.value)
            traverse(node.right)
        traverse(root)
            
    def preorderTraversal(self):
        self.response=[]
        self.preorderTraversal_(self.root)
        return self.response

    def preorderTraversal_(self, root):    
        def traverse(node):
            if node is None:         
                return None  
            self.response.append(node.value)          
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        
    def postorderTraversal(self):
        self.response = []
        self.postorderTraversal_(self.root)
        return self.response
    
    def postorderTraversal_(self, root):      
        def traverse(node):
            if node is None:         
                return None       
            traverse(node.left)
            traverse(node.right)
            self.response.append(node.value)     
        traverse(root)
        
solution = Solution()

# Create a binary search tree 
solution.insert(7)
solution.insert(4)
solution.insert(8)
solution.insert(9)
solution.insert(3)
solution.insert(5)
solution.insert(10) 
solution.insert(2)

inorder_traversed_list = solution.inorderTraversal()
print(f'inorder traversed list : {inorder_traversed_list}')

preorder_traversed_list = solution.preorderTraversal()
print(f'preorder traversed list : {preorder_traversed_list}')

postorder_traversed_list = solution.postorderTraversal()
print(f'postorder traversed list : {postorder_traversed_list}')






