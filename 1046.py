class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heappush(heap, -stone)

        while len(heap) > 1:
            first = heappop(heap)
            second = heappop(heap)
            diff = first - second

            if diff < 0:
                heappush(heap, diff)

        if not heap:
            return 0
        else:
            return -heap[0]
