class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # # Attempt 1: O(nlog(n))
        # citations.sort(reverse=True)
        # for i in range(len(citations)):
        #     if citations[i] >= i + 1:
        #         continue
        #     else:
        #         return i
        # return len(citations)

        # Attempt 2: O(n + k)
        # Create count frequency arr using count sort algorith
        max_val = max(citations)
        count_freq_arr = [0] * (max_val + 1)
        for num in citations:
            count_freq_arr[num] += 1
        
        # Create ordered array
        citations[:] = [] # empty citations array, instead of creating a new one
        for i, count in enumerate(count_freq_arr):
            if not count:
                continue
            citations.extend([i] * count)

        citations.reverse()
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                continue  # Still valid, keep going
            else:
                return i  # Failed at position i, so h-index is i
        return len(citations)  # Never failed → all papers are valid
