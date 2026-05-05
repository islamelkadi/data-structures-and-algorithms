class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                carry = False
                break
            digits[i] = 0
            carry = True
        if carry:
            digits.insert(0, 1)
        return digits
