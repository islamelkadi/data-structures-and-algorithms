from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def numSubarraysWithAtmostSum(nums, goal):
            left = curr = ans = 0
            for right in range(len(nums)):
                curr += nums[right]
                while curr > goal and left <= right:
                    curr -= nums[left]
                    left += 1
                ans += right - left + 1
            return ans
        return numSubarraysWithAtmostSum(nums, goal) - numSubarraysWithAtmostSum(nums, goal - 1)
        # # Build prefix sum array
        # n = len(nums)
        # prefix = [nums[0]]
        # for i in range(1, n):
        #     prefix.append(prefix[-1] + nums[i])

        # # Count subarrays
        # count = 0
        # sum_freq = {0: 1}  # Initialize with 0 sum seen once
        
        # for curr_sum in prefix:
        #     # If we've seen (curr_sum - goal) before,
        #     # it means we can form subarrays with sum = goal
        #     count += sum_freq.get(curr_sum - goal, 0)

        #     # Update frequency
        #     sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1
            
        # return count
