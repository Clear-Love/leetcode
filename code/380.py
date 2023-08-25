from random import choice


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.pos[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            swap_val, idx = self.nums[-1], self.pos[val]
            self.nums[idx] = swap_val
            self.pos[swap_val] = idx
            del self.pos[val]
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.nums)
