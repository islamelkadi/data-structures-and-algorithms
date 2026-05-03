class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        left = 0
        compressed_string = ""
        flush = lambda char, length: char + (str(length) if length > 1 else "")

        for right in range(len(chars)):
            if chars[right] != chars[left]:
                compressed_string += flush(chars[left], right - left)
                left = right
            if right == len(chars) - 1:
                compressed_string += flush(chars[left], right - left + 1)

        for i, char in enumerate(compressed_string):
            chars[i] = char
        return len(compressed_string)