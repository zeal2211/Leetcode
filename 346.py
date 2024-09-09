class MovingAverage:

    def __init__(self, size: int):
        self.averagelist = []
        self.size = size + 1
        self.average = 0

    def next(self, val: int) -> float:
        self.averagelist.append(val)
        self.average += val
        if len(self.averagelist) == self.size:
            first = self.averagelist.pop(0)
            self.average -= first
        return self.average / len(self.averagelist)        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
