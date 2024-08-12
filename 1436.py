class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hashmap = set()
        answer = set()

        for path in paths:
            for city in path[:-1]:
                hashmap.add(city)
                if city in answer:
                    answer.remove(city)
            if path[-1] not in hashmap:
                answer.add(path[-1])

        return list(answer)[0]
            
