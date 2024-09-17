#Milestone 1 Problem11
#Combined Leetcode numbers: 94, 144, 145
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                p  = stack.pop()
                res.append(p.val)
                if p.right:
                    current = p.right
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if root:
                if root.left:
                    traverse(root.left)
                if root.right:
                    traverse(root.right)
                res.append(root.val)
        res = []
        traverse(root)
        return res