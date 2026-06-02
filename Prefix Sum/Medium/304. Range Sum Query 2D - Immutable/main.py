class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

        # Create row based prefix (left to right)
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(1, cols):
                # Where row, col - 1 means same row but the column
                # before it
                matrix[row][col] += matrix[row][col - 1]

        # Create col based prefix (top to bottom)
        for row in range(1, rows):
            for col in range(cols):
                # Where row - 1, col means the same PRIOR row at each
                # new columns
                matrix[row][col] +=  matrix[row - 1][col]

        # Insert left padding
        for row in range(rows):
            matrix[row] = [0] + matrix[row]
        
        # Insert top padding
        # Re-compute number of columns because of added padding,
        # which means an extra column
        cols = len(matrix[0])
        self.matrix = [[0] * cols] + self.matrix

    # def prefixSum(self, array):
    #     prefix = [array[0]]
    #     for i in range(1, len(array)):
    #         prefix.append(array[i] + prefix[-1])
    #     return prefix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        col2 += 1 # Incrementing col2 due to left based padding
        row2 += 1 # Incrementing row2 due to left based padding

        top_range_prefix = self.matrix[row1][col2] - self.matrix[row1][col1]
        bottom_range_prefix = self.matrix[row2][col2] - self.matrix[row2][col1]
        
        return bottom_range_prefix - top_range_prefix

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
