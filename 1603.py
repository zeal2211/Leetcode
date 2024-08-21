class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.curr_big = 0
        self.curr_medium = 0
        self.curr_small = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.curr_big < self.big:
                self.curr_big += 1
                return True
            else:
                return False
        elif carType == 2:
            if self.curr_medium < self.medium:
                self.curr_medium += 1
                return True
            else:
                return False
        else:
            if self.curr_small < self.small:
                self.curr_small += 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
