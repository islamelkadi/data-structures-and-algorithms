from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysWithAtmostKDistinct(nums, k):
            curr = {}
            left = ans = 0
            for right in range(len(nums)):
                curr[nums[right]] = curr.get(nums[right], 0) + 1
                while len(curr) > k and left <= right:
                    curr[nums[left]] -= 1
                    if curr[nums[left]] == 0:
                        del curr[nums[left]]
                    left += 1
                ans += right - left + 1
            return ans
        return subarraysWithAtmostKDistinct(nums, k) - subarraysWithAtmostKDistinct(nums, k - 1)
