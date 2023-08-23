import random
import pyxel

# ## Colors
# Sources:
#   - https://kitao.github.io/pyxel/wasm/examples/05_color_palette.html
#   - https://www.color-name.com/
BLACK = 0
VIRIDIAN_GREEN = 3
BRIGHT_GREY = 7
DOGWOOD_ROSE = 8

# Geometry
WIDTH = HEIGHT = 30
CELL_LENGTH = 20

# Game State
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]

direction = [1, 0]
fruit = [10, 10]
score = 0


def update():
    global snake, direction, fruit, score

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    if pyxel.btnp(pyxel.KEY_DOWN):
        direction = [0, 1]
    elif pyxel.btnp(pyxel.KEY_UP):
        direction = [0, -1]
    elif pyxel.btnp(pyxel.KEY_LEFT):
        direction = [-1, 0]
    elif pyxel.btnp(pyxel.KEY_RIGHT):
        direction = [1, 0]

    head = snake[-1]
    new_head = [head[0] + direction[0], head[1] + direction[1]]
    if (
        new_head in snake
        or new_head[0] < 0
        or new_head[0] >= WIDTH
        or new_head[1] < 0
        or new_head[1] >= HEIGHT
    ):
        pyxel.quit()
    if new_head == fruit:
        score = score + 1
        snake = snake + [new_head]
        fruit = [random.randint(0, 29), random.randint(0, 29)]
    else:
        snake = snake[1:] + [new_head]


def draw():
    pyxel.cls(BRIGHT_GREY)
    for x, y in snake:
        pyxel.rect(x * 20, y * 20, 20, 20, VIRIDIAN_GREEN)
    pyxel.rect(fruit[0] * 20, fruit[1] * 20, 20, 20, DOGWOOD_ROSE)


pyxel.init(
    width=WIDTH * CELL_LENGTH, height=HEIGHT * CELL_LENGTH, title="🐍 Snake Game", fps=5
)
pyxel.run(update, draw)
