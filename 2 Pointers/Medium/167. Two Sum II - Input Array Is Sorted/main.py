class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            summation = numbers[left] + numbers[right]
            if summation < target:
                left += 1
            elif summation > target:
                right -= 1
            else:
                return [left + 1, right + 1]