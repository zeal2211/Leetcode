class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hashmap = collections.Counter(nums)
        self.i = 0

    def showFirstUnique(self) -> int:
        while self.i < len(self.nums):
            curr = self.nums[self.i]
            if self.hashmap[curr] == 1:
                return curr
            self.i += 1
        self.i -= 1
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.hashmap[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
