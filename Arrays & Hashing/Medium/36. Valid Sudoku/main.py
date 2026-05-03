from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        array_length = 9
        grid_length = 3
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        grid_seen = defaultdict(set)

        for row in range(array_length):
            for col in range(array_length):

                if board[row][col] == ".":
                    continue

                if board[row][col] in row_seen[row] or board[row][col] in col_seen[col] or board[row][col] in grid_seen[(row // grid_length, col // grid_length)]:
                    return False
                
                # Add to row
                row_seen[row].add(board[row][col])

                # Add to col
                col_seen[col].add(board[row][col])

                # Add to grid
                grid_seen[(row // grid_length, col // grid_length)].add(board[row][col])
        
        return True