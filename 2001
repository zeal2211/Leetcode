class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hashmap = collections.defaultdict(int)

        for width, height in rectangles:
            hashmap[width/height] += 1

        ans = 0

        for value in hashmap.values():
            if value > 1:
                for i in range(1, value):
                    ans += i

        return ans
