class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        val = len(nums1)
        if m > len(nums1):
            m = len(nums1)
        if n > len(nums2):
            n = len(nums2)
        ans = []
        

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums1.append(nums1[i])
                i += 1
            else: 
                nums1.append(nums2[j])
                j += 1
           
        
        while i < m:
            nums1.append(nums1[i])
            i += 1
        
        while j < n:
            nums1.append(nums2[j])
            j += 1
        
        for _ in range(val):
            nums1.pop(0)
