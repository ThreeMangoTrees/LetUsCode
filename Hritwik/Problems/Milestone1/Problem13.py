# Definition for a binary tree node.
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def findSecondMinimumValue(self, root) -> int:
        def bfs(node):
            queue = [node]
            elements=set()
            while queue:
                for i in range(len(queue)):
                    popped_element = queue.pop(0)
                    if popped_element.left:
                        queue.append(popped_element.left)
                    if popped_element.right:    
                        queue.append(popped_element.right)
                    elements.add(popped_element.val)
            return elements
        elements = list(bfs(root))
        heapq.heapify(elements)
        first_minimum = heapq.heappop(elements)
        while elements:
            second_minimum = heapq.heappop(elements)
            if second_minimum!=first_minimum:
                return second_minimum
        return -1

solution = Solution()

# Create a binary tree to traverse through it in an inorder traversal manner
#
#         Root   2
#              /    \
#             2      5  
#                   /  \
#                  5    7
#
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)


response = solution.findSecondMinimumValue(root)
print(f'The second minimum value in the set made of all the nodes value in the whole tree is {response}')

