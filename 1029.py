class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        total_costs = 0
        n = len(costs)
        for i in range(n // 2):
            total_costs += costs[i][0]
            total_costs += costs[n // 2 + i][1]
        return total_costs
