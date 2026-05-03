class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        string = ""
        for char in s:
            
            # Decode string
            if char == "]":
                decoded_string = ""
                while stack[-1] != "[":
                    # important to preserve the encoded string char order
                    decoded_string = stack.pop() + decoded_string
                # Remove the "[" from the stack
                stack.pop()

                # Decode number
                decoded_number = ""
                while stack and stack[-1].isdigit():
                    decoded_number = stack.pop() + decoded_number
                decoded_number = 1 if not decoded_number else int(decoded_number)

                # Push back onto the stack so 
                stack.append(string + decoded_number * decoded_string)
            else:
                stack.append(char)
        return "".join(stack)
