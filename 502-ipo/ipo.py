import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        # Logic is we store all the profits along with the capital needed in a max heap
        # Continuously pop, if the capital we have is not sufficient we return the element to the heap and get the next one

        for i in range(len(profits)):
            heapq.heappush(max_heap, (-profits[i], capital[i]))

        projects = 0
        old_projects = []
        while projects < k and max_heap != []:
            project = heapq.heappop(max_heap)
            while w < project[1]:
                if max_heap == []:
                    return w
                old_projects.append(project)
                project = heapq.heappop(max_heap)

            projects += 1
            w += -project[0]

            for project in old_projects:
                heapq.heappush(max_heap, project)
            
            old_projects = []

        return w