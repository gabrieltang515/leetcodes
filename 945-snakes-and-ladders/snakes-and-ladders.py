from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        target = n * n

        def get_position(square):
            # Convert square number into row counted from the bottom
            row_from_bottom = (square - 1) // n
            col = (square - 1) % n

            # Every alternate row runs in the opposite direction
            if row_from_bottom % 2 == 1:
                col = n - 1 - col

            # Convert bottom-based row into Python's top-based row index
            row = n - 1 - row_from_bottom

            return row, col

        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            current, moves = queue.popleft()

            if current == target:
                return moves

            for dice_roll in range(1, 7):
                next_square = current + dice_roll

                if next_square > target:
                    break

                row, col = get_position(next_square)

                # Take the snake or ladder immediately
                if board[row][col] != -1:
                    destination = board[row][col]
                else:
                    destination = next_square

                # Only if node is not visited, we explore its neighbours
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))

        return -1