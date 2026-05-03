class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_index = 0
        right_index = len(s) - 1
        
        while left_index < right_index:
            tmp = s[left_index]
            s[left_index] = s[right_index]
            s[right_index] = tmp
            left_index +=1
            right_index -= 1