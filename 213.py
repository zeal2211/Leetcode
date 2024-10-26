class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.r(nums[1:]), self.r(nums[:-1]))
    def r(self, num):
        prev, curr = 0, num[0]

        for n in num[1:]:
            temp = curr
            if n + prev > curr:
                curr = n + prev
            prev = temp

        return curr 
            
            
