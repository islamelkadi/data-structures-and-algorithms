class Solution:
    
    def get_character(self, strs: str, index: int) -> str:
        return strs[index]
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        # Get lens of words in list
        lens = [len(x) for x in strs]
        
        # Get min lens
        min_len = min(lens)
        
        # Get word of min len
        word = strs[lens.index(min_len)]
        
        # Get ith character
        prefix = ""
        for i in range(min_len):
                        
            if len(set([x[i] for x in strs]))==1:
                prefix += word[i]
            else:
                break
                
        return prefix