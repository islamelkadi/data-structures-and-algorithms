class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            component = target - num
            if component in hashmap:
                return [hashmap[component], i]
            hashmap[num] = i