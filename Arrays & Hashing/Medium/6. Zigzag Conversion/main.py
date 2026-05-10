class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        r_tracker, is_down = 0, True
        zig_zag = ["" for _ in range(numRows)]

        for char_ in s:
            zig_zag[r_tracker] += char_
            r_tracker += 1 if is_down else -1
            # If you hit a boundary, then change direction
            if r_tracker in (0, numRows - 1):
                is_down = not is_down

        return "".join(zig_zag)
