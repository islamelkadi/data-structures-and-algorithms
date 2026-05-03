from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_hashmap = Counter(s1)
        s2_hashmap = Counter(s2[:window_size])

        if s1_hashmap == s2_hashmap:
            return True
        
        for i in range(window_size, len(s2)):

            # Add head
            head = s2[i]
            s2_hashmap[head] = s2_hashmap.get(head, 0) + 1

            # Remove tail
            tail = s2[i - window_size]
            s2_hashmap[tail] -= 1
            if s2_hashmap[tail] == 0:
                del s2_hashmap[tail]
            
            # Check permutations
            if s1_hashmap == s2_hashmap:
                return True

        return False