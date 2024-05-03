class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def twoSum(i2, j2, nums, t2):
            m = j2 + 1
            n = len(nums) - 1

            while m < n:
                if nums[m] + nums[n] > t2:
                    n -= 1
                elif nums[m] + nums[n] < t2:
                    m += 1
                else:
                    if [nums[i2],nums[j2],nums[m],nums[n]] not in ans:
                        ans.append([nums[i2],nums[j2],nums[m],nums[n]])
                    n -= 1
                    m += 1

        def threeSum(i1, nums, t1):
            j1 = i1 + 1
            
            while j1 < len(nums):
                twoSum(i1, j1, nums, t1-nums[j1])
                j1 += 1

        for i in range(len(nums)):
            threeSum(i, nums, target-nums[i])

        return ans
