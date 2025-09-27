# from abc import abstractmethod
#
# import pygame
# import random
#
# # Inicjalizacja Pygame
# pygame.init()
#
# # Kolory
# BLUE = (0, 100, 255)  # Gracz
# YELLOW = (255, 255, 0)  # Przedmiot
# BLACK = (0, 0, 0)  # Tło
# WHITE = (255, 255, 255)  # Linia siatki
# RED = (255,0,0)
#
# # Stałe
#
# GRID_SIZE = 15
# TILE_SIZE = 40
# WIDTH = HEIGHT = GRID_SIZE * TILE_SIZE
# FPS = 8
#
#
# class Field:
#     def __init__(self, x, y):
#         self.is_occupied = False
#         self.is_item = False
#         self.is_player = False
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "X" if self.is_occupied else "O"
#
#
# class board:
#     def __init__(self, size):
#         self.size = size
#         self.grid = [[Field for _ in range(size)] for _ in range(size)]
#
#
# class Character:
#     def __init__(self, x, y, defaultCooldown):
#         self.pos = [x, y]
#         self.color = (0, 255, 0)  #GREEN
#         self.defaultCooldown = defaultCooldown
#         self.cooldown = 0
#
#     def move(self, dx, dy):
#         if(self.cooldown == 0):
#             if dx < 0 and self.pos[0] > 0:
#                 self.pos[0] += dx
#             elif dx > 0 and self.pos[0] < GRID_SIZE - 1:
#                 self.pos[0] += dx
#
#             if dy < 0 and self.pos[1] > 0:
#                 self.pos[1] += dy
#             elif dy > 0 and self.pos[1] < GRID_SIZE - 1:
#                 self.pos[1] += dy
#             # self.pos[0] += dx
#             # self.pos[1] += dy
#             self.cooldown += self.defaultCooldown
#
#     def __str__(self):
#         return "C"
#
#     def display(self):
#         pygame.draw.rect(
#             screen,
#             self.color,
#             (self.pos[0] * TILE_SIZE, self.pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
#         )
#
#
# class Player(Character):
#     def __init__(self, x, y, defaultCooldown):
#         super().__init__(x, y, defaultCooldown)
#         self.HP = 100
#         self.boosts = []
#         self.XP = 0
#         self.speed = 1
#         self.color = BLUE
#
#     def execute_cooldown(self):
#         if self.cooldown > 0:
#             self.cooldown -= 1
#         else:
#             self.cooldown = 0
#         print(self.cooldown)
# class Enemy(Character):
#     def __init__(self, x, y,defultCooldown):
#         super().__init__(x, y, defultCooldown)
#         self.damage = 10
#         self.speed = 1
#         self.color = RED
#     def execute_cooldown(self):
#         if self.cooldown > 0:
#             self.cooldown -= 1
#         else:
#             self.cooldown = 0
#
# class Collectible:
#     def __init__(self, x, y):
#         self.pos = [x, y]
#         self.color = (0, 255, 0)  #GREEN
#
#     @abstractmethod
#     def collect(self, player):
#         pass
#
#     def display(self):
#         pygame.draw.rect(
#             screen,
#             self.color,
#             (self.pos[0] * TILE_SIZE, self.pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
#         )
#     def remove(self):
#         self.color = BLACK
#         self.pos = [-1, -1]
#
#
# class HP_Potion(Collectible):
#     def __init__(self,x,y,value):
#         super().__init__(x,y)
#         self.value = value
#     def collect(self, player):
#         player.HP += self.value
#         if player.HP > 100:
#             player.HP = 100
#         print(f"Collected HP Potion! Current HP: {player.HP}")
#
# class Points (Collectible):
#     def __init__(self,x,y,value):
#         super().__init__(x,y)
#         self.value = value
#     def collect(self, player):
#         player.XP += self.value
#         print(f"Collected Points! Current XP: {player.XP}")
#
# class SpeedBoost (Collectible):
#     def __init__(self,x,y,value, amount_of_steps):
#         super().__init__(x,y)
#         self.value = value
#         self.amount_of_steps = amount_of_steps
#
#     def collect(self, player):
#         player.speed += self.value
#         print(f"Collected Speed Boost! Current Speed: {player.speed}")
#
#
# player = Player(GRID_SIZE // 2, GRID_SIZE // 2, 2)
# enemy = Enemy(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1),1)
# enemy1 = Enemy(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1),1)
# enemy2= Enemy(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1),1)
#
# #points = Points(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1), 10)
# collectibles = [
#     Points(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1), 10),
#     HP_Potion(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1), 20)
# ]
# # Tworzenie okna
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Pac-Man Light")
# clock = pygame.time.Clock()
#
# # Pozycja gracza (środek planszy)
# #player_pos = [GRID_SIZE // 2, GRID_SIZE // 2]
#
# # Losowe pole na przedmiot
# # item_pos = [
# #     random.randint(0, GRID_SIZE - 1),
# #     random.randint(0, GRID_SIZE - 1)
# # ]
#
# # Główna pętla gry
# running = True
# while running:
#     clock.tick(FPS)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Czyszczenie ekranu
#     screen.fill(BLACK)
#
#     # Obsługa klawiatury
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player.pos[0] > 0:
#         player.move((-1), 0)
#        # pygame.time.wait(
#         #    100)  #czekamy żeby przy przytrzymaniu klawisza było widać naszego bohatera, dlatego zarażamy grę na 100 ms
#     elif keys[pygame.K_RIGHT] and player.pos[0] < GRID_SIZE - 1:
#         player.move(1, 0)
#
#        # pygame.time.wait(100)
#     elif keys[pygame.K_UP] and player.pos[1] > 0:
#         player.move(0, (-1))
#
#        # pygame.time.wait(100)
#     elif keys[pygame.K_DOWN] and player.pos[1] < GRID_SIZE - 1:
#         player.move(0, 1)
#         #pygame.time.wait(100)
#
#     # Rysowanie siatki
#     for x in range(0, WIDTH, TILE_SIZE):
#         for y in range(0, HEIGHT, TILE_SIZE):
#             pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE), 1)
#
#     # Rysowanie gracza
#     # pygame.draw.rect(
#     #     screen, BLUE,
#     #     (px * TILE_SIZE, py * TILE_SIZE, TILE_SIZE, TILE_SIZE)
#     # )
#     player.display()
#
#     # Rysowanie przedmiotu
#     # ix, iy = item_pos
#     # pygame.draw.rect(
#     #     screen, YELLOW,
#     #     (ix * TILE_SIZE, iy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
#     # )
#     enemy.display()
#     enemy2.display()
#     enemy1.display()
#     for collectible in collectibles:
#         collectible.display()
#         if player.pos == collectible.pos:
#             collectible.collect(player)
#             collectibles.remove(collectible)
#             print(f"Collected {collectible}")
#             break
#
#     enemy.move(random.randint(-1, 1), random.randint(-1, 1))
#     enemy1.move(random.randint(-1, 1), random.randint(-1, 1))
#     enemy2.move(random.randint(-1, 1), random.randint(-1, 1))
#
#     # Sprawdzenie kolizji z przedmiotem
#     if player.pos == enemy.pos:
#         print("Enemy hit!")
#         player.HP -= enemy.damage
#         print(f"Player HP: {player.HP}")
#         if player.HP <= 0:
#             print("Game Over")
#             running = False
#
#     # Sprawdzenie kolizji z przedmiotem
#     if player.pos == enemy2.pos:
#         print("Enemy hit!")
#         player.HP -= enemy2.damage
#         print(f"Player HP: {player.HP}")
#         if player.HP <= 0:
#             print("Game Over")
#             running = False
#
#     # Sprawdzenie kolizji z przedmiotem
#     if player.pos == enemy1.pos:
#         print("Enemy hit!")
#         player.HP -= enemy1.damage
#         print(f"Player HP: {player.HP}")
#         if player.HP <= 0:
#             print("Game Over")
#             running = False
#
#     player.execute_cooldown()
#     enemy.execute_cooldown()
#     enemy2.execute_cooldown()
#     enemy1.execute_cooldown()
#
#
#     # Aktualizacja ekranu
#     pygame.display.flip()
#
# # Zakończenie gry
# pygame.quit()
from entity import Character, player, Enemy, RegularEnemy, SmartEnemy, \
    FastEnemy, Punktak, HealthPotion, Speed, screen, fontEndgame, fontSmall, Meteor
from board import board
from config import*
import pygame
import random

# region initializing statics

REG_DMG = [AVG_DMG_REGULAR//2, 3*AVG_DMG_REGULAR//2]
SMART_DMG = [AVG_DMG_SMART//2, 3*AVG_DMG_SMART//2]
FAST_DMG = [AVG_DMG_FAST//2, 3*AVG_DMG_FAST//2]

AVG_PTS = [AVG_PTS//2, 3*AVG_PTS//2]
AVG_HP = [AVG_HP//2, 3*AVG_HP//2]
AVG_MOVES = [AVG_MOVES//2, 3*AVG_MOVES//2]


pygame.display.set_caption("Pac-Man Light")
clock = pygame.time.Clock()
tick = 0
# endregion
# region main loop
running = True
closeImmediatelyAfterLeavingTheLoop = False
board.add_entity(player)
while running:
    clock.tick(FPS)
    tick += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            closeImmediatelyAfterLeavingTheLoop = True
            break

    # region keyboard inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1, 0)
    elif keys[pygame.K_RIGHT]:
        player.move(1, 0)
    elif keys[pygame.K_UP]:
        player.move(0, -1)
    elif keys[pygame.K_DOWN]:
        player.move(0, 1)
    elif keys[pygame.K_q]:
        player.move(-1, -1)
    elif keys[pygame.K_w]:
        player.move(1, -1)
    elif keys[pygame.K_a]:
        player.move(-1, 1)
    elif keys[pygame.K_s]:
        player.move(1, 1)

    # endregion

    # region in-game logic
    if (tick-1) % SPAWN_INTERVAL == 0:
        # region spawning enemies
        chance_of_spawn = chanceOfSpawn(tick)
        if random.random() < chance_of_spawn:
            # probability of spawning a regular enemy: 32/tick
            if random.random() < regularEnemySpawnChance(tick):
                field = board.randomUnoccupiedField()
                board.add_entity(
                    RegularEnemy(field[0], field[1], random.randint(REG_DMG[0], REG_DMG[1]), REG_CD)
                )
            elif random.random() < smartEnemySpawnChance(tick):
                field = board.randomUnoccupiedField()
                board.add_entity(
                    SmartEnemy(field[0], field[1], random.randint(SMART_DMG[0], SMART_DMG[1]), SMART_CD)
                )
            else:
                field = board.randomUnoccupiedField()
                board.add_entity(
                    FastEnemy(field[0], field[1], random.randint(FAST_DMG[0], FAST_DMG[1]), FAST_CD)
                )
        # endregion
        # region spawning collectibles
        if random.random() < COLLECTIBLE_SPAWN_CHANCE:
            field = board.randomUnoccupiedField()
            if random.random() < POINT_SPAWN_CHANCE:
                board.add_entity(
                    Punktak(board.getField(field[0], field[1]), random.randint(AVG_PTS[0], AVG_PTS[1]))
                )
            elif random.random() < HP_SPAWN_CHANCE:
                board.add_entity(
                    HealthPotion(board.getField(field[0], field[1]), random.randint(AVG_HP[0], AVG_HP[1]))
                )
            elif random.random() < METEOR_SPAWN_CHANCE:  # Add teleportation spawn chance
                board.add_entity(
                    Meteor(board.getField(field[0], field[1]))
                )
            else:
                board.add_entity(
                    Speed(board.getField(field[0], field[1]), random.randint(AVG_MOVES[0], AVG_MOVES[1]))
                )
        # endregion
    for entity in board.entities:
        if isinstance(entity, Character):
            entity.execute_cooldown()
        if isinstance(entity, Enemy):
            entity.move()

    if player.HP <= 0:
        running = False
    # endregion

    # region displaying
    screen.fill(BLACK)
    for x in range(0, WIDTH, TILE_SIZE):
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.rect(screen, GRAY, (x, y, TILE_SIZE, TILE_SIZE), 1)
    for entity in board.entities:
        entity.display()
    score = fontSmall.render("Score: " + str(player.score), True, WHITE)
    screen.blit(score, (0, 0))
    pygame.display.flip()
    # endregion
# endregion
# region after the game is over
if not closeImmediatelyAfterLeavingTheLoop:
    end_text = fontEndgame.render(str(player.score), True, WHITE)
    text_rect = end_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(end_text, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
pygame.quit()
# endregion