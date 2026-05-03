class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                # Note: do not do b // a because this will always
                # round down to the lowest nearest negative. If you
                # have positive numbers then no problem, but if you
                # have negatives and did -7 / -2 you will end up with
                # -4 instead of -3
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        return stack.pop()
