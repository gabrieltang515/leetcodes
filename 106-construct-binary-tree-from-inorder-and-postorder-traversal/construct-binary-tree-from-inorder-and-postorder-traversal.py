# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        inorder_index = {}

        for i, val in enumerate(inorder):
            inorder_index[val] = i

        self.postorder_index = len(postorder) - 1

        def build(left, right):
            # no nodes in this subtree
            if left > right:
                return None

            # preorder gives us the root first
            root_val = postorder[self.postorder_index]
            self.postorder_index -= 1

            root = TreeNode(root_val)

            # find root position in inorder
            mid = inorder_index[root_val]

            # build left side first, because preorder is root-left-right
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)