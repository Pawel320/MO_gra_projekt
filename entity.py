import random
from abc import abstractmethod
import pygame

from board import board
from config import PLAYER_HP, NORMAL_MODE_COLOUR, SPEED_MODE_COLOUR, RED, BLUE, TILE_SIZE, WHITE, GRID_SIZE, \
    PLAYER_COOLDOWN, YELLOW, \
    WIDTH, HEIGHT, FONT_SIZE, RADIUS


def paint_square(x, y, color):
    pygame.draw.rect(
        screen,
        color,
        (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    )


pygame.init()
fontEndgame = pygame.font.SysFont("Arial", 200)
fontSmall = pygame.font.SysFont("Arial", FONT_SIZE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_img = pygame.image.load("Bohaterowie/player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (TILE_SIZE, TILE_SIZE))

player_speed_img = pygame.image.load("Bohaterowie/player_speed.png").convert_alpha()
player_speed_img = pygame.transform.scale(player_speed_img, (TILE_SIZE, TILE_SIZE))

enemy_img = pygame.image.load("Bohaterowie/enemy.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (TILE_SIZE, TILE_SIZE))

enemy_smart_img = pygame.image.load("Bohaterowie/enemy_smart.png").convert_alpha()
enemy_smart_img = pygame.transform.scale(enemy_smart_img, (TILE_SIZE, TILE_SIZE))

enemy_fast_img = pygame.image.load("Bohaterowie/enemy_fast.png").convert_alpha()
enemy_fast_img = pygame.transform.scale(enemy_fast_img, (TILE_SIZE, TILE_SIZE))

collectible_img = pygame.image.load("Bohaterowie/collectible.png").convert_alpha()
collectible_img = pygame.transform.scale(collectible_img, (TILE_SIZE, TILE_SIZE))

helth_img = pygame.image.load("Bohaterowie/health_potion_img.png").convert_alpha()
class Entity:
    def __init__(self, x, y):
        self.field = board.getField(x, y)
        self.field.entity = self

    @abstractmethod
    def display(self):
        pass


class Character(Entity):
    def __init__(self, x, y, default_cooldown):
        super().__init__(x, y)
        self.cooldown = 0
        self.default_cooldown = default_cooldown

    @abstractmethod
    def display(self):
        pass

    def execute_cooldown(self):
        if self.cooldown >= 1:
            self.cooldown -= 1
        else:
            self.cooldown = 0

    def teleport(self, x, y):
        field = board.getField(x, y)
        if field != 0:
            self.field.clear()
            self.field = field
            field.entity = self


class Player(Character):
    def __init__(self, x, y, default_cooldown):
        super().__init__(x, y, default_cooldown)
        self.HP = PLAYER_HP
        self.XP = 0
        self.score = 0
        self.diagonal_moves = 0

    def display(self):
        if self.diagonal_moves == 0:
            screen.blit(player_img, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))
        else:
            screen.blit(player_speed_img, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))
        pygame.draw.rect(screen, RED,
                         (self.field.x * TILE_SIZE, (self.field.y + .9) * TILE_SIZE,
                          (self.cooldown / self.default_cooldown) * TILE_SIZE, .1 * TILE_SIZE)
                         )

        hp_text = fontSmall.render(str(self.HP), True, WHITE)
        screen.blit(hp_text, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))

    def take_damage(self, damage):
        self.HP -= damage


    def enter_a_nonempty_field(self, entity):
        if isinstance(entity, Enemy):
            self.take_damage(entity.damage)
            entity.field.clear()
            board.entities.remove(entity)
        elif isinstance(entity, Collectible):
            if isinstance(entity, HealthPotion):
                self.HP += entity.HP
            elif isinstance(entity, Punktak):
                self.score += entity.points
            # elif isinstance(entity, teleportation):
            #     entity.teleport_player(self)
            elif isinstance(entity, Speed):
                self.diagonal_moves += entity.diagonal_moves
            if isinstance(entity, Meteor):
                entity.explode()
            else:
                entity.field.clear()
            board.entities.remove(entity)

    def move(self, dx, dy):
        if self.cooldown > 0:
            return
        if dx != 0 and dy != 0:
            if self.diagonal_moves == 0:
                return
            else:
                self.diagonal_moves -= 1
        field = board.getField(self.field.x + dx, self.field.y + dy)
        if field != 0:
            if field.entity is not None:
                self.enter_a_nonempty_field(field.entity)
            self.teleport(self.field.x + dx, self.field.y + dy)
            self.cooldown += self.default_cooldown


player = Player(GRID_SIZE // 2, GRID_SIZE // 2, PLAYER_COOLDOWN)


class Enemy(Character):
    def __init__(self, x, y, damage, default_cooldown):
        super().__init__(x, y, default_cooldown)
        self.damage = damage
        self.default_cooldown = default_cooldown

    def destroy(self):
        self.field.clear()
        board.entities.remove(self)

    @abstractmethod
    def display(self):
        #paint_square(self.field.x, self.field.y, RED)
        pass

    @abstractmethod
    def move(self):
        pass


class RegularEnemy(Enemy):

    def move(self):
        if self.cooldown == 0:
            dx = random.randint(-1, 1)
            if dx == 0:
                if random.getrandbits(1):
                    dy = -1
                else:
                    dy = 1
            else:
                dy = 0
            field = board.getField(self.field.x + dx, self.field.y + dy)
            if field != 0:
                if field.entity is not None and isinstance(field.entity, Player):
                    field.entity.take_damage(self.damage)
                    self.destroy()
                else:
                    if field.entity is not None:
                        board.entities.remove(field.entity)
                        field.clear()
                    self.teleport(self.field.x + dx, self.field.y + dy)
                    self.cooldown += self.default_cooldown

    def display(self):
        super().display()
        # noinspection SpellCheckingInspection
        text = fontSmall.render("Regu", True, WHITE)
        screen.blit(enemy_img, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))


class SmartEnemy(Enemy):
    def move(self):
        if self.cooldown == 0:
            if self.field.x - player.field.x < 0:
                dx = 1
            elif self.field.x - player.field.x > 0:
                dx = -1
            else:
                dx = 0
            if dx == 0:
                if self.field.y - player.field.y < 0:
                    dy = 1
                else:
                    dy = -1
            else:
                dy = 0
            field = board.getField(self.field.x + dx, self.field.y + dy)
            if field != 0:
                if field.entity is not None and isinstance(field.entity, Player):
                    field.entity.take_damage(self.damage)
                    self.destroy()
                else:
                    if field.entity is not None:
                        board.entities.remove(field.entity)
                        field.clear()
                    self.teleport(self.field.x + dx, self.field.y + dy)
                    self.cooldown += self.default_cooldown

    def display(self):
        super().display()
        text = fontSmall.render("Smart", True, WHITE)
        screen.blit(enemy_smart_img, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))


class FastEnemy(Enemy):
    def move(self):
        if self.cooldown == 0:
            if random.random() < .5:
                # 50% chance of moving in the general direction of the player
                if self.field.x - player.field.x < 0:
                    dx = 1
                elif self.field.x - player.field.x == 0:
                    dx = 0
                else:
                    dx = -1
                if self.field.y - player.field.y < 0:
                    dy = 1
                elif self.field.y - player.field.y == 0:
                    dy = 0
                else:
                    dy = -1
            else:
                dx = random.randint(-1, 1)
                dy = random.randint(-1, 1)
            if dx == dy == 0:
                return

            field = board.getField(self.field.x + dx, self.field.y + dy)
            if field != 0:
                if field.entity is not None and isinstance(field.entity, Player):
                    field.entity.take_damage(self.damage)
                    self.destroy()
                else:
                    if field.entity is not None:
                        board.entities.remove(field.entity)
                        field.clear()
                    self.teleport(self.field.x + dx, self.field.y + dy)
                    self.cooldown += self.default_cooldown

    def display(self):
        super().display()
        text = fontSmall.render("Fast", True, WHITE)
        screen.blit(enemy_fast_img, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))


class Collectible(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def display(self):
        screen.blit(collectible_img, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))


# noinspection SpellCheckingInspection
class Punktak(Collectible):
    def __init__(self, field, points):
        super().__init__(field.x, field.y)
        self.points = points

    def display(self):
        super().display()
        hp_text = fontSmall.render("Pts:" + str(self.points), True, RED)
        screen.blit(collectible_img, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))


class HealthPotion(Collectible):
    def __init__(self, field, hp):
        super().__init__(field.x, field.y)
        self.HP = hp

    def display(self):
        super().display()
        hp_text = fontSmall.render("HP:" + str(self.HP), True, RED)
        screen.blit(helth_img, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))


class Speed(Collectible):
    def __init__(self, field, num_of_diagonal_moves):
        super().__init__(field.x, field.y)
        self.diagonal_moves = num_of_diagonal_moves

    def display(self):
        super().display()
        hp_text = fontSmall.render("S:" + str(self.diagonal_moves), True, RED)
        screen.blit(hp_text, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))


# class teleportation(Collectible):
#     def __init__(self, field):
#         super().__init__(field.x, field.y)
#         self.field2 = board.randomUnoccupiedField()
#
#         self.fields[0].entity = self
#         self.fields[1].entity = self
#
#     def display(self):
#         paint_square(self.fields[0].x, self.fields[0].y, BLUE)
#         paint_square(self.fields[1].x, self.fields[1].y, BLUE)
#         tp_text = fontSmall.render("TP", True, RED)
#         screen.blit(tp_text, (self.fields[0].x * TILE_SIZE, self.fields[0].y * TILE_SIZE))
#         screen.blit(tp_text, (self.fields[1].x * TILE_SIZE, self.fields[1].y * TILE_SIZE))
#
#     def teleport_player(self, player):
#         if player.field == self.fields[0]:
#             player.teleport(self.fields[1].x, self.fields[1].y)
#         elif player.field == self.fields[1]:
#             player.teleport(self.fields[0].x, self.fields[0].y)

class Meteor(Collectible):
    def __init__(self,field):
        super().__init__(field.x, field.y)
        self.radius = RADIUS

    def explode(self):
        print("Exploding")
        for entity in board.entities:
            if not isinstance(entity, Player) and not isinstance(entity, Meteor):
                distance = ((entity.field.x - self.field.x) ** 2 + (entity.field.y - self.field.y) ** 2) ** 0.5
                if distance <= self.radius:
                    entity.field.clear()
                    board.entities.remove(entity)
    def display(self):
        super().display()
        hp_text = fontSmall.render("BUM:" + str(self.radius), True, RED)
        screen.blit(hp_text, (self.field.x * TILE_SIZE, self.field.y * TILE_SIZE))