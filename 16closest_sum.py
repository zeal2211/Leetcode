class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        output = 0 
        difference = float("inf")       

        for c in range(len(nums)):
            first = nums[c]
            i = c + 1
            j = len(nums) - 1

            while i < j:
                second = nums[i]
                third = nums[j]
                curr_sum = first + second + third
                curr_diff = abs(target - curr_sum)
                if curr_sum > target:
                    j -= 1
                elif curr_sum < target:
                    i += 1
                else:
                    return curr_sum
                if curr_diff < difference:
                    difference = curr_diff
                    output = curr_sum

        return output
