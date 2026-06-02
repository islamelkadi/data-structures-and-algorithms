class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        alphabet_len = len(alphabet)
        
        dic = {letter for letter in sentence}
        return alphabet_len == len(dic)
