class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_width = 0
        points.sort()
        for i in range(len(points) - 1):
            max_width = max(max_width, points[i+1][0] - points[i][0])

        return max_width
            