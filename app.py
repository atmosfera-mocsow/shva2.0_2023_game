import pygame

SIZE = (800, 600)
step = 20

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False

clock = pygame.time.Clock()


class LPaddle():
    _x = 0
    _y = 0
    _w = 0
    _h = 0
    def __init__(self, screen_size, step):
        self._w = screen_size[0] // 20
        self._h = screen_size[1] // 5
        self._y = screen_size[1] // 2
        self.__step = step

    def up(self):
        self._y -= self.__step

    def down(self):
        self._y += self.__step

class RPaddle():
    _x = 0
    _y = 0
    _w = 0
    _h = 0

    def __init__(self, screen_size, step):
        self._w = screen_size[0] // 20
        self._h = screen_size[1] // 5
        self._y = screen_size[1] // 2
        self._x = screen_size[0] - self._w
        self.__step = step

    def up(self):
        self._y -= self.__step

    def down(self):
        self._y += self.__step
     
class Ball():
    _x = 0
    _y = 0
    _rad = 30
    _flip = 1
    _flipY = 1
    _step = 2
    def __init__(self, screen_size):
        self._x = screen_size[0] // 2
        self._y = screen_size[1] // 2

    def flip(self):
        self._flip *= -1


    def flip_st(self):
        self._flipY *= -1

    def move_x(self):
        self._x += self._step*self._flip
        self._y += self._step*self._flipY

    def __repr__(self):
        print("Ball: ", self._x, self._y, self._flip, self._flipY)



lp = LPaddle(SIZE, step)
rp = RPaddle(SIZE, step)
ball = Ball(SIZE)


ball.flip()
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        lp.up()
    if pressed[pygame.K_DOWN]:
        lp.down()
    if pressed[pygame.K_LEFT]:
        rp.up()
    if pressed[pygame.K_RIGHT]:
        rp.down()

    
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, pygame.Rect(lp._x, lp._y, lp._w, lp._h))
    pygame.draw.rect(screen, WHITE, pygame.Rect(rp._x, rp._y, rp._w, rp._h))
    pygame.draw.circle(screen, WHITE, (ball._x, ball._y), ball._rad)

    ball.move_x()

    if ((ball._x-ball._rad) <= (lp._x+lp._w)):
        if (ball._y > lp._y) and (ball._y < (lp._y+lp._h)):
            ball.flip()

    if ((ball._x+ball._rad) >= (rp._x)):
        if (ball._y > rp._y) and (ball._y < (rp._y+rp._h)):
            ball.flip()

    if (ball._y-ball._rad) <= 0:
        ball.flip_st()
        print(ball._x, ball._y, ball._flip, ball._flipY)

    if (ball._y+ball._rad) >= SIZE[1]:
        ball.flip_st()

    if ((ball._x+ball._rad) >= (rp._x)):
        print("GAME OVER")

    if ((ball._x-ball._rad) <= (lp._x+lp._w)):
        print("GAME OVER")
    


    pygame.display.flip()
    clock.tick(60)