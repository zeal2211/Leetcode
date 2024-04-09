class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 1
        curr = 1
        i = 1
        prev = nums[0]

        while i < len(nums):
            if nums[i] != prev:
                prev = nums[i]
                ans += 1
                nums[curr] = nums[i]
                curr += 1
            i += 1
        
        return ans
