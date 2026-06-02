class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort array
        nums.sort()

        # Find triplets
        triplets = []
        nums_len = len(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left = i+1
            right = nums_len - 1

            while left < right:
                summation = nums[i] + nums[left] + nums[right]
                if summation < 0:
                    left +=1
                elif summation > 0:
                    right -= 1
                else:
                    triples = [nums[i], nums[left], nums[right]]
                    triplets.append(triples)
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
        return triplets