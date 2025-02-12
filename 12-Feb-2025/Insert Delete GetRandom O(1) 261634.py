# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.randomized_set = {}

    def insert(self, val: int) -> bool:

        # if the val is already in the randomized_set
        if self.randomized_set.get(val) is not None:
            return False

        self.randomized_set[val] = val
        return True

    def remove(self, val: int) -> bool:

        # check if the val exists in the randomized_set
        if self.randomized_set.get(val) is None:
            return False

        del self.randomized_set[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(list(self.randomized_set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()