class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suffix = prefix = 1
        ans = float("-inf")
        n = len(nums)
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            ans = max(ans, prefix, suffix)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        return ans