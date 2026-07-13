from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        visited = set()
        queue = deque([(startGene, 0)])
        choices = ["A", "C", "G", "T"]

        while queue:
            
            variant = queue.popleft()
            currentgene, mutation = variant

            if currentgene == endGene:
                return mutation

            for i in range(len(currentgene)):
                for char in choices:
                    if currentgene[i] == char:
                        continue

                    new_mutation = currentgene[:i] + char + currentgene[i+1:]

                    if new_mutation in bank and new_mutation not in visited:
                        queue.append((new_mutation, mutation + 1))
                        visited.add(new_mutation)

        return -1