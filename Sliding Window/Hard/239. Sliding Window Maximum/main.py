import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # # First attempt
        # max_elements = []
        # nums = [-x for x in nums]
        # for i in range(0, len(nums) - k + 1):
        #     heap = nums[i : i + k]
        #     heapq.heapify(heap)
        #     max_elements.append(-heap[0])
        # return max_elements

        # Second attempt - more optimized
        # Step 1
        # Notice that we are using the heap
        # to store the element and its index
        # this is because heaps behave lexograpically
        # and you don't want to lose the duplicate entry
        # incase the list had a duplicate entry. The fact
        # that you need to find the max heap and that heaps
        # allow lexographic comparision is why we also made
        # the index negative so that if the first entry is
        # a duplicate, then you do a lexographic comparison
        # on the second entry and you choose the bigger one
        # accordingly to be the heap max. If the question
        # wanted min heap, then you won't need to do a negative
        # number nor a negative index, you would use it as is.
        # Python's heapq doesn't support max heap, hence the
        # negative addition
        if k == 1:
            return nums

        heap = []
        heapq.heapify(heap)
        for i in range(k):
            heapq.heappush(heap, (-nums[i], -i))

        # Add max element
        max_elements = [-heap[0][0]]

        # Step 2
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], -i))

            # This means that the left most boundary's index
            # is still greater than that of the current heap
            # max. This means the heap is no longer within
            # bounds
            while i - k >= -heap[0][1]:
                heapq.heappop(heap)

            max_elements.append(-heap[0][0])
        return max_elements
