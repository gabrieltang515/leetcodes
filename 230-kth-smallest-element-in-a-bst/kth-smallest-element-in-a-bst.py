# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        result = []

        def in_order(node):
            if node is None:
                return 
            
            if node.left:
                left = in_order(node.left)

            result.append(node.val)

            if node.right:
                right = in_order(node.right)
            
        in_order(root)

        return result[k-1]
