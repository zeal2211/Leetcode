class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashmap = collections.defaultdict(int)
        left = 0
        max_subarray = 0

        for right, num in enumerate(nums):
            hashmap[num] += 1
            while hashmap[num] > k:
                hashmap[nums[left]] -= 1
                left += 1 

            max_subarray = max(max_subarray, right - left + 1)
        
        
        return max_subarray
            
