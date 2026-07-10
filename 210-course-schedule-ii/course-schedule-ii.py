from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        path = []
        visiting = set()
        visited = set()

        graph = defaultdict(list)

        # prereq -> course
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        def dfs(course):
            if course in visiting:
                # Cycle detected
                return False

            if course in visited:
                # Already completely processed
                return True

            visiting.add(course)

            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False

            # Backtracking: course is no longer in current DFS route
            visiting.remove(course)
            visited.add(course)

            # Add only after processing everything after it
            path.append(course)

            return True

        # Must check every course, including isolated courses
        for course in range(numCourses):
            if not dfs(course):
                return []

        return path[::-1]