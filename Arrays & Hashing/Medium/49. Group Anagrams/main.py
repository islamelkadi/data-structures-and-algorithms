from collections import defaultdict, Counter, OrderedDict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # Notice the requirements: string only consists of english letters
        #     # This maybe a clue to use 26 fixed chars
        # alphabets = "abcdefghijklmnopqrstuvwxyz"
        # alphabets_indexed = {key: index for index, key in enumerate(alphabets)}

        # grouped_anagrams = defaultdict(list)
        # for str_ in strs:
        #     alphabets_array = [0] * 26
        #     counted_str = Counter(str_)
        #     for alphabet, frequency in counted_str.items():
        #         alphabets_array[alphabets_indexed[alphabet]] = frequency
        #     grouped_anagrams[tuple(alphabets_array)].append(str_)
        
        # return list(grouped_anagrams.values())
        grouped_anagrams = defaultdict(list)
        for str_ in strs:
            alphabets_array = [0] * 26
            for alphabet in str_:
                alphabets_array[ord(alphabet) - ord("a")] += 1
            grouped_anagrams[tuple(alphabets_array)].append(str_)
        return list(grouped_anagrams.values())