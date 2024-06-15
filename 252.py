class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[0])
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            x = interval[0]
            prev_y = intervals[i-1][1]
            
            if x < prev_y:
                return False

        return True
