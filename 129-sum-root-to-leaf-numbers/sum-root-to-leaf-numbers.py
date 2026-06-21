# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):

        def dfs(node, curr):
            if node is None:
                return 0
            
            curr = curr * 10 + node.val

            # leaf node
            if node.left is None and node.right is None:
                return curr
            
            left_sum = dfs(node.left, curr)
            right_sum = dfs(node.right, curr)

            return left_sum + right_sum
        
        return dfs(root, 0)