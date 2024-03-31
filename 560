class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, total = 0, 0
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1

        for num in nums:
            total += num
            if total - k in hashmap:
                count += hashmap[total - k]
            hashmap[total] += 1

        return count
            
