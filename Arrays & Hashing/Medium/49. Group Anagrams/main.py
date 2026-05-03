from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # # Option 1 - sorted string as hashmap key
        # anagram_hashmap = defaultdict(list)
        # for word in strs:
        #     ordered_word = "".join(sorted(word))
        #     anagram_hashmap[ordered_word].append(word)
        # return list(anagram_hashmap.values())

        # Option 2 - Char to index mapping
        anagram_hashmap = defaultdict(list)
        for word in strs:
            word_chars_index = [0] * 26
            for str_ in word:
                word_chars_index[ord(str_) - ord("a")] += 1
            anagram_hashmap[tuple(word_chars_index)].append(word)
        return list(anagram_hashmap.values())