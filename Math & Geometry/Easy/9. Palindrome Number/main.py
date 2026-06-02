class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_2 = x
            rev = 0
            while x_2 > 0:
                rev = x_2 % 10 + rev * 10
                x_2 //= 10
            return x == rev
