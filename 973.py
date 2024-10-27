import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        

        for x, y in points:
            dis = -(math.pow(x,2) + math.pow(y,2))
            heappush(heap, (dis, [x,y]))
            if len(heap) > k:
                heappop(heap)

        return [x[1] for x in heap]
