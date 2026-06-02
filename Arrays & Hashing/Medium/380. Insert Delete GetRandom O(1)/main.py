import random

class RandomizedSet(object):

    def __init__(self):
        self.array = []
        self.hashmap = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False

        self.hashmap[val] = len(self.hashmap)
        self.array.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            return False

        index = self.hashmap[val]
        is_last_index = (index == len(self.array) - 1)
        last_element = self.array.pop()
        if not is_last_index:
            self.array[index] = last_element
            self.hashmap[last_element] = index

        del self.hashmap[val]
        return True

    def getRandom(self):
        """
        :type: int
        """
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
