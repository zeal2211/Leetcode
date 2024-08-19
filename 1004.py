class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        ans = 0
        swapped = 0

        while j < len(nums):
            if nums[j] == 0:
                swapped += 1
                while swapped > k:
                    if nums[i] == 0:
                        swapped -= 1
                    i += 1
            ans = max(ans, j - i + 1)
            j += 1


        return ans
