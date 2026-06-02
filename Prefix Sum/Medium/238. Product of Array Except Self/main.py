class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Prefix array
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] * prefix[-1])

        # Suffix array
        suffix = [1] * n
        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]

        # Return products
        for i in range(n):
            if i == 0:
                nums[i] = 1 * suffix[i + 1]
            elif i == n - 1:
                nums[i] = prefix[i - 1] * 1
            else:
                nums[i] = prefix[i - 1] * suffix[i + 1]
        return nums
