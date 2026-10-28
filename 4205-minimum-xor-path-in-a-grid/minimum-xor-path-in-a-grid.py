class Solution(object):
    def minCost(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        # states[c] holds the XOR values reaching the current row's
        # cell at column c.
        states = [set() for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                value = grid[r][c]

                if r == 0 and c == 0:
                    states[c] = {value}
                else:
                    # Before updating, states[c] is from above.
                    # states[c - 1] is from the left in this row.
                    previous = states[c]
                    if c > 0:
                        previous = previous | states[c - 1]

                    states[c] = {x ^ value for x in previous}

        return min(states[-1])