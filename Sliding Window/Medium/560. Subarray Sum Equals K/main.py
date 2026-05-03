from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = curr = 0
        prefix_hashmap = defaultdict(int)
        prefix_hashmap[0] = 1

        # Build prefix array & hashmap
        for num in nums:
            curr += num

            # target = sum[i] (i.e curr) - sum[j] (i.e previous curr)
            # you have the target, you have the curr, you need to find sum[j]
            # sum[j] = target - sum[i]
            ans += prefix_hashmap[curr - k]
            prefix_hashmap[curr] += 1

        return ans