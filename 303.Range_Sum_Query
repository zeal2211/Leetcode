class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.prefix = [0 for _ in range(len(nums) + 2)]
        for i in range(len(self.arr)):
            self.prefix[i+1] = self.prefix[i] + self.arr[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
