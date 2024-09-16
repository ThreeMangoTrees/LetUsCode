#Milestone 1Problem 10:Leetcode number 102(https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
# Time: O(N), Space O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        if root:
            seen = 0
            queue.append([root, 0])
            while queue:
                node, lvl = queue.pop(0)
                if seen==0 or seen<lvl:
                    res.append([node.val])
                    seen = lvl
                else:
                    res[lvl].append(node.val)
                if node.left:
                    queue.append([node.left,lvl+1])
                if node.right:
                    queue.append([node.right,lvl+1])
        return res