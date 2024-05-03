class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = [0 for _ in range(len(prices))]
        curr_min = prices[0]

        for i in range(len(prices)):
            if i < len(prices) - 1:
                if prices[i+1] < prices[i]:     
                    total[i] =  prices[i] - curr_min
                    curr_min = prices[i+1]
            else:
                total[i] = max(0, prices[i] - curr_min)

        return sum(total)
