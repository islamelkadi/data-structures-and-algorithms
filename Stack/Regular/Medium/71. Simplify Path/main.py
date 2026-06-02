class Solution:
    def simplifyPath(self, path: str) -> str:
        # splitting by a `/` delimeter will resolve multiple back to back slashes
        stack = []
        for dir_ in path.split("/") :
            # If dir_ is current `'.'` or empty string because of the delimeter split then continue
            if dir_ == "." or dir_ == "":
                continue
            if dir_ != "..":
                stack.append(dir_)
            elif stack:
                stack.pop()
        return "/" + "/".join(stack)
