class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        split_word = list(word)
        found = []
        rows = len(board)
        columns = len(board[0])
        visited = set()

        def backtracking(found, split_word, r, c):

            if "".join(found) == word:
                return True

            if r < 0 or r >= rows or c < 0 or c >= columns or split_word == []:
                return False

            letter = board[r][c]
            found_it = False

            if letter == split_word[0] and (letter, r, c) not in visited:
                found.append(split_word.pop(0))
                visited.add((letter, r, c))
                found_it = backtracking(found, split_word, r + 1, c) or backtracking(found, split_word, r - 1, c) or backtracking(found, split_word, r, c + 1) or backtracking(found, split_word, r, c - 1)

                visited.remove((letter, r, c))
                split_word.insert(0, letter)
                found.pop()
            else:
                return False

            return found_it

        for i in range(rows):
            for j in range(columns):
                if backtracking(found, split_word, i, j):
                    return True

        return False

        