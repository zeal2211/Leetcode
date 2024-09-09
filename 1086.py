import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)

        for item in items:
            id = item[0]
            score = item[1]
            if len(hashmap[id]) == 5:
                if hashmap[id][0] < score:
                    heappop(hashmap[id])
                    heappush(hashmap[id], score)
            else:
                heappush(hashmap[id], score)

        ans = []

        for key, value in hashmap.items():
            ans.append([key, sum(value)//5])

        return sorted(ans, key=lambda x: x[0])
