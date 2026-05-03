class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Your code goes here
        nums.sort()
        triplets = set()
        target_sum = 0
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target_sum:
                    triplets.add((nums[i], nums[left], nums[right]))
                
                if current_sum < target_sum:
                    left += 1
                else:
                    right -=1
        return list(triplets)