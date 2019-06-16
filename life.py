

# class Cell:
#     def __init__(self, x, y, is_alive=False):
#         Before Turtle, print out an X,Y grid?
#         self.x = x
#         self.y = y
#         self.is_alive = is_alive

#     def __str__(self):
#         if self.is_alive:
#             print("X")
#         else:
#             print("O")

ALIVE = 'O'
DEAD = 'X'

class Game:
    def __init__(self, width, height, seed=None):
        self.width = width
        self.height = height
        self.seed = seed
        self.grid = [[ALIVE for x in range(self.width)] for y in range(self.height)]

    def __str__(self):
        output_str = ""
        for row in self.grid:
            for cell in row:
                output_str += cell + " "
            output_str += "\n"

        return output_str

    def set_cell(self, x, y, is_alive):
        self.grid[y][x] = DEAD if is_alive else ALIVE

    def count_neighbors(self, x, y):
        count = 0
        count += self.grid[y-1][x-1] == ALIVE
        count += self.grid[y-1][x]   == ALIVE
        count += self.grid[y-1][x+1] == ALIVE
        count += self.grid[y][x-1]   == ALIVE
        count += self.grid[y][x+1]   == ALIVE
        count += self.grid[y+1][x-1] == ALIVE
        count += self.grid[y+1][x] == ALIVE
        count += self.grid[y+1][x+1] == ALIVE
        return count



game = Game(5,5)
game.set_cell(1, 2, True)
game.set_cell(1, 3, True)
game.set_cell(1, 4, True)
print(game)

print(game.count_neighbors(0,0))

