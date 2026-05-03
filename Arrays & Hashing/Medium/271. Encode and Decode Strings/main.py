class Codec:
    def __init__(self):
        self.delim = "#"

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""

        encoded_string = ""
        for str_ in strs:
            encoded_string += str(len(str_)) + self.delim + str_
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []

        decoded_string_list = []
        current_index = 0
        string_len = ""
        while current_index < len(s):
            if s[current_index] != self.delim:
                string_len += s[current_index]
            else:
                decoded_string_list.append(s[current_index + 1: current_index + 1 + int(string_len)])
                current_index += int(string_len)
                string_len = ""
            current_index += 1
        return decoded_string_list


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))