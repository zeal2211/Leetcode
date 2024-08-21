class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        i = 1
        c = 1

        while c < n:
            if (intervals[i-1][1] >= intervals[i][0]) :    
                intervals[i-1][1] = intervals[i][1] if intervals[i][1] > intervals[i-1][1] else intervals[i-1][1]
                intervals.pop(i)
                c += 1
                continue
            i += 1 
            c += 1


        return intervals
