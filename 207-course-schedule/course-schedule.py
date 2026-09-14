class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        visiting = set()

        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        def dfs(course):
            if course in visiting:
                # cycle detected here
                return False
            
            if course in visited:
                return True # already checked, no cycle from here. a tad bit of wishful thinking

            visiting.add(course)
            for cor in graph[course]:
                if not dfs(cor):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False



        return True

            
        

            