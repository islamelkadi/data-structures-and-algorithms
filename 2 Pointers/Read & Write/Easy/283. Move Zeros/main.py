class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        while right <= len(nums) - 1: # Needed to move the very last index of the array
            # Check if left index == 0 and right index != 0
                # Switch
                # increment both left and right
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right += 1

            # Check if left index != 0 and right index == 0:
                # No switch
                # increment both left and right
            elif nums[left] != 0 and nums[right] == 0:
                left +=1
                right += 1

            # Check if left index != 0 and right index != 0:
                # No switch
                # increment both left and right
            elif nums[left] != 0 and nums[right] != 0:
                left +=1
                right += 1

            # Check if left index == 0 and right index == 0:
                # No switch
                # increment right
            else:
                right += 1