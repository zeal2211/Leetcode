class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            val = abs(nums[abs(num)-1])
            nums[abs(num)-1] = - val

        ans = []

        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i+1)

        return ans
