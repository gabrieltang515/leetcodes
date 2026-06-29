# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = []
        queue = deque([root])
        direction = True

        while queue:

            level = []
            no_of_nodes = len(queue)

            for i in range(no_of_nodes):

                if direction: #From L to R
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)

                else: # From R to L
                    node = queue.pop()
                    level.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                        
                    if node.left:
                        queue.appendleft(node.left)
                    

                    
            direction = not direction
            result.append(level)

        return result

                



        