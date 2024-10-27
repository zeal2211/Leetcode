import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) == k:
                if num > heap[0]:
                    heappushpop(heap, num)
            else:
                heappush(heap, num)

        return heap[0]
