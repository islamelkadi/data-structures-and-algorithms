from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row_index = 0
        final_ans = 0
        for i, row in enumerate(mat):
            total_sum = sum(row)
            if total_sum > final_ans:
                row_index = i
                final_ans = total_sum
        return [row_index, final_ans]
