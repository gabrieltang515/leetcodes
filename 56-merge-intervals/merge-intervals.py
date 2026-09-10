class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        last_start = intervals[0][0]
        last_end = intervals[0][1]

        result = []

        for i in range(1, len(intervals)):

            current_start = intervals[i][0]
            current_end = intervals[i][1]

            if current_start <= last_end:
                # overla exists
                last_end = max(current_end, last_end)
            else:
                result.append([last_start, last_end])
                last_start = current_start
                last_end = current_end

        result.append([last_start, last_end])
        return result