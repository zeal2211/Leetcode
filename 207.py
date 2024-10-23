class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        zero = []

        nodes = defaultdict(list)
        indegree = defaultdict(int)

        for course, prereq in prerequisites:
            nodes[prereq].append(course)
            indegree[course] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                zero.append(i)

        visited = 0
        while zero:
            curr_node = zero.pop(0)
            visited += 1
            for node in nodes[curr_node]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    zero.append(node)


        return visited == numCourses

                

                
