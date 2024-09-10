import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        ans = 0

        while len(sticks) > 1:
            top1 = heappop(sticks)
            top2 = heappop(sticks)
            total = top1 + top2
            ans += total
            heappush(sticks, total)

        return ans
