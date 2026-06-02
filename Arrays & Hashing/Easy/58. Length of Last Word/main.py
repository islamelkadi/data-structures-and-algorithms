class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_encountered_yet = False
        letters_encountered = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                letter_encountered_yet = True
            
            if letter_encountered_yet and s[i].isalpha():
                letters_encountered += 1
            
            if s[i] == " " and letter_encountered_yet:
                break
        return letters_encountered
