class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Solution 1 - time exceeded
        # while k != 0:
        #     nums.insert(0, nums.pop())
        #     k -= 1
        # 
 
        # # Solution 2 - 2 pointers
        # nums.reverse()
        # k = k % len(nums)
        # left, right_1_ptr = 0, k - 1
        # k_ptr, right_2_ptr = k, len(nums) - 1

        # while left < right_1_ptr:
        #     nums[left], nums[right_1_ptr] = nums[right_1_ptr], nums[left]
        #     left += 1
        #     right_1_ptr -= 1
        
        # while k_ptr < right_2_ptr:
        #     nums[k_ptr], nums[right_2_ptr] = nums[right_2_ptr], nums[k_ptr]
        #     k_ptr += 1
        #     right_2_ptr -= 1

        # Solution 3 - 2 pointers abstracted
        nums.reverse()

        # Get pivot index
        k = k % len(nums)
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
