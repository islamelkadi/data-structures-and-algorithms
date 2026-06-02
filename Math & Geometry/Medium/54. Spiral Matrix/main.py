class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        spiral = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        while top < bottom and left < right:

            # Traverse top row (left to right)
            for i in range(left, right):
                spiral.append(matrix[top][i])
            top += 1

            # Traverse right column (top to bottom)
            for i in range(top, bottom):
                spiral.append(matrix[i][right - 1])
            right -= 1

            # Traverse bottom row (right to left)
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    spiral.append(matrix[bottom - 1][i])
                bottom -=1

            # Traverse left column (bottom to top)
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    spiral.append(matrix[i][left])
                left += 1

        return spiral
