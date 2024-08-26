class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.response = []
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        # Get the middle element of the sorted element to divide the array into two parts
        new_node=TreeNode(nums[len(nums)//2]) 
        new_node.left=self.sortedArrayToBST(nums[:len(nums)//2])
        new_node.right=self.sortedArrayToBST(nums[len(nums)//2+1:])
        return new_node
    def inOrderTraversal(self, root):
        def traverse(node):
            if root is None:
                return None
            if node.left:
                traverse(node.left)
            self.response.append(node.val)
            if node.right:
                traverse(node.right)
        traverse(root)
        return self.response

solution = Solution()
nums = [-10,-3,0,5,9]
response_head = solution.sortedArrayToBST(nums)
response = solution.inOrderTraversal(response_head)
print(f'InOrder Traversal of Height-balanced binary search tree of the given array: {response}')
