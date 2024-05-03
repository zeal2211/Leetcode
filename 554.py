class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        total_gaps = {0:0}

        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                total_gaps[total] = 1 + total_gaps.get(total, 0)

        return len(wall) - max(total_gaps.values())
