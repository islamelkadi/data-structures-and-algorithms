from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)

        # Pre-compute the prefix sum
        prefix_sum_array = [nums[0]]
        for i in range(1, nums_len):
            prefix_sum_array.append(prefix_sum_array[-1] + nums[i])

        # Calculate averages for entries where we
        # know for sure that there is a valid window
        averages_array = [-1] * nums_len
        window_size = 2 * k + 1
        for i in range(k, nums_len - k):
            if i == k: # This is for the very first entry of the window:
                window_sum = prefix_sum_array[i + k]
            else:
                # Note that we add a -1 to i - k - 1 because if we don't then the
                # window will be INCLUSIVE of the i-kth element, but we must drop
                # that so that you have the sum of all the previous values to the
                # i-kth value without including it so we don't mess up the average
                # calculations
                window_sum = prefix_sum_array[i + k] - prefix_sum_array[i - k - 1]
            averages_array[i] = window_sum // window_size
        return averages_array
