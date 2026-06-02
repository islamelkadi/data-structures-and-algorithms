class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Logic:
        # Create a hashset of all the items in the list
        # Iterate through each entry in the hashset, and find
        # out which ones do not have an n-1 in the hashset.
        # Those will be your starting points, and you can enforce
        # the starting point check via an if condition to continue
        # into the logic if that particular number does not have a
        # n-1.

        # Once you've passed the check, from there:
            # 1. Initialize a counter of len 1
            # 2. Check if n+1 exists in hashset
            # 3. If yes increment the subarr_len
            # 4. Increment num
            # 5. Iterate to the next num
        nums_hashset = set(nums)
        ans = 0
        for num in nums_hashset:
            if num - 1 not in nums_hashset:
                subarr_len = 1
                while num + 1 in nums_hashset:
                    subarr_len += 1
                    num += 1
                ans = max(ans, subarr_len)
        return ans