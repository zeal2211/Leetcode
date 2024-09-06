class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.board = set()
        self.snake = [[0, 0]]
        self.food = food
        self.board.add((0, 0))
        self.score = 0
        self.height = height
        self.width = width

    def lost(self, i, j):
        if i >= self.height or i < 0 or j >= self.width or j < 0:
            return True
        if (i,j) in self.board:
            return True

        return False 

    def move(self, direction: str) -> int:
        position = self.snake[-1]
        first_pos = self.snake.pop(0)
        fi, ji = first_pos[0], first_pos[1]

        self.board.remove((fi,ji))
        i, j = position[0], position[1]
        if direction == 'R':
            j += 1
        elif direction == 'L':
            j -= 1
        elif direction == 'U':
            i -= 1
        else:
            i += 1
        if self.lost(i, j):
            return -1

        self.board.add((i,j))
        self.snake.append([i, j])
        

        if self.food and [i, j] == self.food[0]:
            self.food.pop(0)
            self.snake.insert(0, first_pos)
            self.board.add((fi, ji))
            self.score += 1

        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
