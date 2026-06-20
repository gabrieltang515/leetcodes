# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        dummy = TreeNode(0)
        dummy_ptr = [dummy]

        def preorder(node):
            if node is None:
                return

            left = node.left
            right = node.right

            dummy_ptr[0].right = node
            dummy_ptr[0] = dummy_ptr[0].right
            dummy_ptr[0].left = None

            preorder(left)
            preorder(right)

        preorder(root)
        