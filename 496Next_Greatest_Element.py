class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[0]]
        hashmap = {}

        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                hashmap[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while stack:
            hashmap[stack.pop()] = -1

        return [hashmap[num] for num in nums1]
