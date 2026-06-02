class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## READ ME:
        # The problem with the below implementation is that you are storing space in O(n)
        # complexity. This is because you need to create an entry for every item in the
        # range of n. I'm not sure why this is here as it cannot be solved using hash set
        # or hash map and meet the O(1) time complexity.

        # n = len(nums)
        # nums_set = set(nums)
        # n_range = {x for x in range(n+1)}
        # for num in n_range:
        #     if num not in nums_set:
        #         return num

        # Alternative solution:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
