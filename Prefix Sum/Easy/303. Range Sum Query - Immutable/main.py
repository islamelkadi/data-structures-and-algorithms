class NumArray:

    def __init__(self, nums: List[int]):
        self._prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self._prefix_sum.append(nums[i] + self._prefix_sum[-1])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sum[right]
        # The left - 1 is because you do not want to include left
        # this is because you would essentially subtracting the
        # prefix sum with the left pointer being considered, when
        # it should be up until the left pointer but not including
        # it.
        return self._prefix_sum[right] - self._prefix_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)