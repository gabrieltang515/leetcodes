class Solution:
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:

        def isIdentical(node1, node2):
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False

            return (
                node1.val == node2.val
                and isIdentical(node1.left, node2.left)
                and isIdentical(node1.right, node2.right)
            )

        if subRoot is None:
            return True

        if root is None:
            return False

        if isIdentical(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )