import heapq
from typing import List

class Solution:
    def kSmallestPairs(
        self,
        nums1: List[int],
        nums2: List[int],
        k: int
    ) -> List[List[int]]:

        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        result = []

        # Add the first pair from each relevant row.
        for i in range(min(k, len(nums1))):
            pair_sum = nums1[i] + nums2[0]

            heapq.heappush(
                heap,
                (pair_sum, i, 0)
            )

        while heap and len(result) < k:
            pair_sum, i, j = heapq.heappop(heap)

            result.append([nums1[i], nums2[j]])

            # Reveal the next pair from the same row.
            if j + 1 < len(nums2):
                next_sum = nums1[i] + nums2[j + 1]

                heapq.heappush(
                    heap,
                    (next_sum, i, j + 1)
                )

        return result