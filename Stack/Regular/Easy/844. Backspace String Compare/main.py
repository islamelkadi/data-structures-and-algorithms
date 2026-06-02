class Solution:
    def delete_char(self, string: str):
        stack = []
        for char in string:
            if char != "#":
                stack.append(char)
            elif char == "#" and stack:
                stack.pop()
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:  
        return self.delete_char(s) == self.delete_char(t)
