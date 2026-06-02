class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        len_rows, len_cols = len(matrix), len(matrix[0])

        # Check if there are zeros in the first row
        first_row_zero = 0 in matrix[0]
        first_col_zero = any(matrix[r][0] == 0 for r in range(len_rows))

        # Pass 1: mark target rows / cols
        for row in range(len_rows):
            for col in range(len_cols):
                if matrix[row][col] == 0:
                    # To avoid a needless overwrite check if both
                    # the first row or col of that target are 0
                    # if yes continue, else overwrite
                    # if matrix[0][col] == 0 and matrix[row][0] == 0:
                    #     continue
                    
                    # A more concise (but less readable) way of the above
                    # commented out condition is as follows:
                    if (matrix[0][col] or matrix[row][0]) == 0:
                        continue
                    matrix[0][col] = matrix[row][0] = 0

        # BUG - you need to ignore the first
        # row and columns or you will accidentally
        # interpret recently zeroed out markers
        # as the new ground truth
        # Pass 2: set rows to zero
        for row in range(1, len_rows):
            for col in range(1, len_cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_zero:
            matrix[0][:] = [0] * len_cols

        if first_col_zero:
            for row in range(len_rows):
                matrix[row][0] = 0
