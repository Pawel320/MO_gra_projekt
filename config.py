import math

NORMAL_MODE_COLOUR = (160, 160, 160)  # Colour of player in normal mode (RGB)
SPEED_MODE_COLOUR = (0, 153, 51)  # Colour of player in speed mode
YELLOW = (255, 255, 0)  # Colour of collectible
BLUE = (184, 215, 233)  # Colour of teleportation portal
BLACK = (0, 0, 0)  # Background colour
WHITE = (255, 255, 255)  # Text colour
RED = (255, 0, 0)  # Enemy colour
GRAY = (30, 30, 30)  # Gridlines colour
GRID_SIZE = 14  # Number of tiles in length & height of the board
TILE_SIZE = 70  # Square tile side size (in pixels)
WIDTH = HEIGHT = GRID_SIZE * TILE_SIZE  # board size (in pixels)
FONT_SIZE = 24  # Regular font size
FPS = 32  # FPS and ticks per second
RADIUS = 3 #Bomb radius

PLAYER_HP = 100  # Player HP at start of the game
AVG_DMG_REGULAR = 6  # Average damage of a regular enemy (will vary in AVG_DMG_REGULAR * [0.5, 1.5])
AVG_DMG_SMART = 8  # Average damage of a smart enemy -||-
AVG_DMG_FAST = 4  # Average damage of a fast enemy -||-

PLAYER_COOLDOWN = 8  # Player movement cooldown
REG_CD = 16  # Average regular enemy movement cooldown (will vary +-1)
SMART_CD = 15  # Average smart enemy movement cooldown -||-
FAST_CD = 12  # Average fast enemy movement cooldown -||-

AVG_PTS = 10  # Average collectible points (will vary from 0.5 to 1.5 *AVG_PTS)
AVG_HP = 5  # Average HP of a health potion -||-
AVG_MOVES = 5  # Average num of diagonal moves of a speed potion -||-

SPAWN_INTERVAL = 256  # Number of ticks between spawns of collectibles & enemies
COLLECTIBLE_SPAWN_CHANCE = 1  # Probability of a collectible spawning in an interval
POINT_SPAWN_CHANCE = .5  # Probability of a point collectible spawning in an interval (if bomb and HP did not spawn)
HP_SPAWN_CHANCE = .5  # Probability of a HP potion collectible spawning in an interval (if bomb did not spawn)
METEOR_SPAWN_CHANCE = 0.4  # Probability of a teleportation portal spawning in an interval


def chanceOfSpawn(tick):  # chance of an enemy spawn function (must vary from 0 to 1 for tick=1,2,...)
    return 1 - 1 / math.sqrt(tick)


def regularEnemySpawnChance(tick):  # chance of a regular enemy spawning. If not, a smart will try to spawn
    return 32/tick


def smartEnemySpawnChance(tick):  # chance of a smart enemy spawning (provided regular one didn't spawn)
    # If not, a fast WILL spawn
    return 0.5
