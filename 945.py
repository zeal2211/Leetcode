class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        print(nums)

        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                output += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1

        return output
