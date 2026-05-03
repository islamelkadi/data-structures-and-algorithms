class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = zero_counter = max_array_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_counter += 1
            
            while zero_counter > 1:
                if nums[left] == 0:
                    zero_counter -=1
                left += 1

            max_array_len = max(max_array_len, right - left + 1)
        return max_array_len