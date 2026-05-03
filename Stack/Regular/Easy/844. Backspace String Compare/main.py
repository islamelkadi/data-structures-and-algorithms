class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            stack = []
            for c in string:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack
        return process(s) == process(t)
