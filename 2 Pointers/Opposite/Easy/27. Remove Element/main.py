from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums) - 1
        for left in range(len(nums)):
            while nums[right] == val and right >= 0:
                right -= 1
            # Should be left > right instead of
            # left == right because you may have
            # use cases where the list is even.
            # Therefore, you won't have a situation
            # where left == right when you right -= 1
            # and left += 1
            if left > right:
                break
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return right + 1
