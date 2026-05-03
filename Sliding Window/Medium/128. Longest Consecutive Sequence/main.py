class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_hashset = set(nums)
        ans = 0
        for num in nums_hashset:
            if num - 1 not in nums_hashset:
                subarr_len = 1
                while num + 1 in nums_hashset:
                    subarr_len += 1
                    num += 1
                ans = max(ans, subarr_len)
        return ans