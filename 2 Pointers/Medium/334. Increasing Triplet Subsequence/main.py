class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = second_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num # lower the first gate
            elif num <= second_smallest:
                second_smallest = num   # lower the second gate (num already passed gate 1)
            else:
                return True # num passed both gates → triplet exists
        return False
