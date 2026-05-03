class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[slow_pointer] = nums[slow_pointer], nums[i]
                slow_pointer += 1
        return nums