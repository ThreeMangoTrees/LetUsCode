# Create a Binary Search Tree and Do Pre/In/Post Oder traversal of the tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.arr = []

    def insert_node(self,node,val):
        if node.val > val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.insert_node(node.left,val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self.insert_node(node.right,val)
    def add_node(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.insert_node(self.root,val)

    def _in_order(self,node):
        if node:
            if node.left:
                self._in_order(node.left)
            self.arr.append(node.val)
            if node.right:
                self._in_order(node.right)

    def in_order(self):
        self.arr = []
        self._in_order(self.root)
        return self.arr

    def _pre_order(self,node):
        if node:
            self.arr.append(node.val)
            if node.left:
                self._pre_order(node.left)
            if node.right:
                self._pre_order(node.right)

    def pre_order(self):
        self.arr = []
        self._pre_order(self.root)
        return self.arr

    def _post_order(self,node):
        if node:
            if node.left:
                self._post_order(node.left)
            if node.right:
                self._post_order(node.right)
            self.arr.append(node.val)

    def post_order(self):
        self.arr = []
        self._post_order(self.root)
        return self.arr

arr = [3,1,2,5,6,4]
bst = BST()
for i in arr:
    bst.add_node(i)
print(bst.in_order())
print(bst.pre_order())
print(bst.post_order())
