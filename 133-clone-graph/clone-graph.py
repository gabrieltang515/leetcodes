"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        hashmap = {} #stores original node -> new node mapping
        if node is None:
            return None

        def dfs(node):
            if node in hashmap:
                return hashmap[node]

            clone = Node(node.val, [])
            hashmap[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone


        return dfs(node)


