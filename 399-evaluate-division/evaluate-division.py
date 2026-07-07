from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        graph = defaultdict(list)

        # Build graph
        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]

            graph[a].append((b, value))        # a / b = value
            graph[b].append((a, 1.0 / value))  # b / a = 1 / value

        def dfs(curr, target, visited, product):
            if curr == target:
                return product

            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited, product * weight)

                    if result != -1.0:
                        return result

            return -1.0

        ans = []

        for a, b in queries:
            # If either variable does not exist, impossible
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(a, b, set(), 1.0))

        return ans