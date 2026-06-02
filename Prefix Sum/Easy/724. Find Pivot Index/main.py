from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # # Option 1 - prefix_sum & suffix_sum arrays
        # prefix_sum = [nums[0]]
        # for i in range(1, len(nums)):
        #     prefix_sum.append(prefix_sum[-1] + nums[i])

        # suffix_sum = [0] * len(nums)
        # suffix_sum[-1] = nums[-1]
        # # You are doing len(nums) - 2 because you have alread
        # # factored the len(nums) - 1 index above in right_sum
        # for i in range(len(nums) - 2, -1, -1):
        #     suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        # # Find index of equal summation
        # for i in range(len(nums)):
        #     if prefix_sum[i] == suffix_sum[i]:
        #         return i

        # return -1

        # Option 2 - single pass computation of suffix_sum
        prefix_sum = suffix_sum = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            if prefix_sum == total - prefix_sum - nums[i]:
                return i
            prefix_sum += num
        return -1
