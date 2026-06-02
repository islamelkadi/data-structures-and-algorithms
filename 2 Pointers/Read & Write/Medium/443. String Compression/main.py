from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        
        while read < len(chars):
            char = chars[read]
            group_length = 0
            
            # Count the length of the current group
            while read < len(chars) and chars[read] == char:
                read += 1
                group_length += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if it's greater than 1
            if group_length > 1:
                for digit in str(group_length):
                    chars[write] = digit
                    write += 1
                    
        return write