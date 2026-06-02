import heapq
import math

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Since largest is required, converting list to negative
        nums = [-n for n in nums]
        heapq.heapify(nums)

        # Note in previous submissions you were trying to find the
        # index of the target node using the formula for 0-indexed
        # array -> left: 2N + 1 | right: 2N + 2
        # Heaps are not sorted in the sense of traditional sorted
        # arrays, so you cannot rely on that mechanism. Instead,
        # when you pop an element, the heap will recorrect itself
        # to maintain the proper heap tree structure. So in theory,
        # if you pop k - 1 times (because you still want to arrive
        # at that Kth element, so make sure to not pop that out) you
        # will theoritically have the kth's largest element as the
        # root of the tree

        # NOTE: I hate to break it to you, but this is at worst case
        # O(nlog(n)). In other words, there is not difference between
        # 1) heapifying this
        # and
        # 2) doing a nums.sorted(reverse=True) and then picking nums[k]
        for _ in range(k - 1):
            heapq.heappop(nums)
        
        return -nums[0]
