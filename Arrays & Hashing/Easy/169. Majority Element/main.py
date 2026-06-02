class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Approach 1
        # candidate, vote = nums[0], 1
        # for i in range(1, len(nums)):
        #     if nums[i] == candidate:
        #         vote += 1
        #     else:
        #         vote -= 1
            
        #     if not vote:
        #         candidate = nums[i]
        #         vote = 1
        # return candidate

        # Approach 2 - more elegant
        candidate = vote = 0
        for num in nums:
            if vote == 0:
                candidate = num
            vote += 1 if candidate == num else -1
        return candidate
