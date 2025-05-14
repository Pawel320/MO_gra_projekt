import pygame
import random

# Inicjalizacja Pygame
pygame.init()

# Kolory
BLUE = (0, 100, 255)  # Gracz
YELLOW = (255, 255, 0)  # Przedmiot
BLACK = (0, 0, 0)  # Tło
WHITE = (255, 255, 255)  # Linia siatki

# Stałe

GRID_SIZE = 15
TILE_SIZE = 40
WIDTH = HEIGHT = GRID_SIZE * TILE_SIZE
FPS = 60


class Field:
    def __init__(self, x, y):
        self.is_occupied = False
        self.is_item = False
        self.is_player = False
        self.x = x
        self.y = y

    def __str__(self):
        return "X" if self.is_occupied else "O"


class board:
    def __init__(self, size):
        self.size = size
        self.grid = [[Field for _ in range(size)] for _ in range(size)]


class Character:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.color = (0, 255, 0)  #GREEN

    def move(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

    def __str__(self):
        return "C"

    def display(self):
        pygame.draw.rect(
            screen,
            self.color,
            (self.pos[0] * TILE_SIZE, self.pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )


class Player(Character):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.HP = 100
        self.boosts = []
        self.XP = 0
        self.speed = 1
        self.color = BLUE


class Enemy(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.damage = 10
        self.speed = 1
        self.color = YELLOW


player = Player(GRID_SIZE // 2, GRID_SIZE // 2)
enemy = Enemy(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

# Tworzenie okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Light")
clock = pygame.time.Clock()

# Pozycja gracza (środek planszy)
#player_pos = [GRID_SIZE // 2, GRID_SIZE // 2]

# Losowe pole na przedmiot
# item_pos = [
#     random.randint(0, GRID_SIZE - 1),
#     random.randint(0, GRID_SIZE - 1)
# ]

# Główna pętla gry
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Czyszczenie ekranu
    screen.fill(BLACK)

    # Obsługa klawiatury
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.pos[0] > 0:
        player.move((-1), 0)
        pygame.time.wait(
            100)  #czekamy żeby przy przytrzymaniu klawisza było widać naszego bohatera, dlatego zarażamy grę na 100 ms
    elif keys[pygame.K_RIGHT] and player.pos[0] < GRID_SIZE - 1:
        player.move(1, 0)

        pygame.time.wait(100)
    elif keys[pygame.K_UP] and player.pos[1] > 0:
        player.move(0, (-1))

        pygame.time.wait(100)
    elif keys[pygame.K_DOWN] and player.pos[1] < GRID_SIZE - 1:
        player.move(0, 1)
        pygame.time.wait(100)

    # Rysowanie siatki
    for x in range(0, WIDTH, TILE_SIZE):
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE), 1)

    # Rysowanie gracza
    # pygame.draw.rect(
    #     screen, BLUE,
    #     (px * TILE_SIZE, py * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    # )
    player.display()

    # Rysowanie przedmiotu
    # ix, iy = item_pos
    # pygame.draw.rect(
    #     screen, YELLOW,
    #     (ix * TILE_SIZE, iy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    # )
    enemy.display()

    # Aktualizacja ekranu
    pygame.display.flip()

# Zakończenie gry
pygame.quit()
