class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_symbol_reference = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Approach 1 - stack
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        # stack = []
        # for char_ in s:
        #     if stack and roman_symbol_reference[char_] > stack[-1]:
        #         stack.append(roman_symbol_reference[char_] - stack.pop())
        #     else:
        #         stack.append(roman_symbol_reference[char_])
        # return sum(stack)

        # Time Complexity: O(N)
        # Space Complexity: O(1)
        previous = summation = 0
        for char_ in s:
            if roman_symbol_reference[char_] > previous:
                # Logic here is to FIRST undo the addition of previous integer
                # Then add the difference between the current integer and the one before it

                # Instead of doing summation -= previous then roman[char_] - previous
                # you can do - (previous * 2) since you are subtracting previous twice
                summation -= previous * 2
            summation += roman_symbol_reference[char_]
            previous = roman_symbol_reference[char_]
        return summation
