# We're trying to find the MAXIMUM LENGTH of a subarray
# When we find a prefix_sum - k in curr, we calculate length as: right - curr[seen]
# Setting curr[0] = -1 helps us handle the case where the subarray starts from index 0
# Example: if nums = [1,2,3] and k = 6, when we reach index 2, prefix_sum = 6
# We look for prefix_sum - k = 6 - 6 = 0
# Length = 2 - (-1) = 3, giving us the correct length for [1,2,3]

# THIS IS A LENGTH CALCUATION PROBLEM
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        # # Build prefix sum array
        # prefix_sum = [nums[0]]
        # for i in range(1, len(nums)):
        #     prefix_sum.append(nums[i] + prefix_sum[-1])
        
        # # Build prefix sum to index hashmap
        # curr = {0: -1}
        # for i, value in enumerate(prefix_sum):
        #     if value not in curr:
        #         curr[value] = i
        
        # # Get max len
        # ans = 0
        # for right in range(len(nums)):
        #     seen = prefix_sum[right] - k
        #     if seen in curr:
        #         ans = max(ans, right - curr[seen])
        # return ans

        prefix_sum = ans = 0
        curr = {0: -1}  # Initialize with 0 sum at index -1

        for right in range(len(nums)):
            prefix_sum += nums[right]
            if prefix_sum not in curr:
                curr[prefix_sum] = right
            seen = prefix_sum - k
            if seen in curr:
                ans = max(ans, right - curr[seen])
        return ans