class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[0])
        ans = 1
        high = points[0][1]
        
        for i in range(1, len(points)):
            temp_high = points[i][1]
            if points[i][0] <= high:
                if high > temp_high:
                    high = temp_high
            else:
                ans += 1
                high = temp_high
            
        return ans

        
