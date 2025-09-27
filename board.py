import random

from config import GRID_SIZE


class Field:
    def __init__(self, x, y):
        self.entity = None
        self.x = x
        self.y = y

    def clear(self):
        self.entity = None

    def populate(self, entity):
        self.entity = entity


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[Field(j, i) for i in range(size)] for j in range(size)]
        self.entities = []
        self.collectibles = []

    def getField(self, x, y):
        if 0 <= x < self.size:
            if 0 <= y < self.size:
                return self.grid[x][y]
        return 0

    def execute_cooldowns(self):
        pass

    def add_entity(self, entity):
        self.entities.append(entity)

    def randomUnoccupiedField(self):
        for i in range(1, 100):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.grid[x][y].entity is None:
                return [x, y]


board = Board(GRID_SIZE)
