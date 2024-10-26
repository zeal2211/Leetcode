class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]

        flag = False

        col = 0

        while col < n:
            if obstacleGrid[0][col] == 1:
                flag = True
            if flag:
                dp[0][col] = 0
            col += 1

        row = 0
        flag = False
        while row < m:
            if obstacleGrid[row][0] == 1:
                flag = True
            if flag:
                dp[row][0] = 0
            row += 1        


        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

        
