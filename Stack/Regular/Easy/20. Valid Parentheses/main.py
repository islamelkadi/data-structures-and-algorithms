class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets_stack = []
        opening_brackets_hashmap = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        for bracket in s:
            if bracket in opening_brackets_hashmap:
                opening_brackets_stack.append(bracket)
            else:
                if not opening_brackets_stack:
                    return False
                
                previous_opening_bracket = opening_brackets_stack.pop()
                if bracket != opening_brackets_hashmap[previous_opening_bracket]:
                    return False
        return not opening_brackets_stack
