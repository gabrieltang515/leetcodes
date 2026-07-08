class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = set()
        # Build graph first
        graph = defaultdict(list)

        for course in prerequisites:
            actual, prereq = course
            graph[prereq].append(actual)
        
        visiting = set()
        visited = set()

        # DFS should conduct cycle finding
        def dfs(course):
            if course in visiting:
                return False  # cycle found

            if course in visited:
                return True   # already checked, no cycle from here

            visiting.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # Backtracking idea here
            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True



            
            


            