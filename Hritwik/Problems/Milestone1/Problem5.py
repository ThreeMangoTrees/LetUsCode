# Definition for a binary tree node.
class Node:
    def __init__(self, value:int):
        self.value = value
        self.left = None
        self.right = None

# # Create a binary tree to check symmetry
# #
# #         Root   1
# #              /    \
# #             2      3  
# #            / \    /  \
# #           4   5  6    7
# #          /
# #         8
# #
# root=Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.left.left.left= Node(8)

# Create a symmetric binary tree to check symmetry
#
#         Root   1
#              /    \
#             2      2  
#            / \    /  \
#           4   5  5    4
#          /   /    \    \
#         8   1      1    8
#
root=Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(5)
root.right.right = Node(4)
root.left.left.left= Node(8)
root.left.right.left= Node(1)
root.right.left.right= Node(1)
root.right.right.right= Node(8)

class Solution:
    def isSymettric(self, root: Node) -> bool:
        if root is None:
            return True

        def isMirror(first:Node, second:Node) -> bool:
            if first is None and second is None:
                return True
            if first is None or second is None:
                return False
            if first.value != second.value:
                return False
            return isMirror(first.left, second.right) and isMirror(first.right, second.left)
        
        return isMirror(root.left, root.right)

solution = Solution()
response_tree = solution.isSymettric(root)
print(f'The tree is symmetric (True or False) : {response_tree}')
