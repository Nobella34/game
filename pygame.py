import random
import math
import pygame

# constants
WINSIZE = [640, 480]
WINCENTER = [320, 240]
NUMSTARS= 150

width = 360
height = 480

def init_star():
    "creates new star values"
    dir = random.randrange(100000)
    velmult = random. random() * 0.6 + 0.4
    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult]
    return vel, WINCENTER[:]


def initialize_stars():
    "creates a new starfield"
    stars = []
    for x in range(NUMSTARS):
        star = init_star()
        vel, pos = star
        steps = random.randint(0, WINCENTER[0])
        pos[0] = pos [0] + (vel[0] * steps)
        pos[1] = pos[1] + (vel[1] * steps)
        vel[0] = vel[0] * (steps * 0.09)
        vel[1] = vel[1] * (steps * 0.09)
        stars.append(star)
    move_stars(stars)
    return stars


def draw_stars(surface, stars, color):
    "used to draw (and clear) the stars"
    for vel, pos in stars:
        pos = (int(pos[0]), int(pos[1]))
        surface.set_at(pos, color)


def move_stars(stars):
    "animate the star values"
    for vel, pos in stars:
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        if not 0 <= pos[0] <= WINSIZE[0] or not 0<= pos[1] <= WINSIZE[1]:
            vel[:], pos[:] = init_star()
        else:
            vel[0] = vel[0] * 1.05
            vel[1] = vel[1] * 1.05

def main():
    "This is the starfield code"
    # create our starfield
    random.seed()
    stars = initialize_stars()
    clock = pygame.time.Clock()
    # initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption("pygame Stars Example")
    white = 255, 240, 200
    black= 20, 20, 40
    screen.fill(black)

    # main game loop
    screen.fill(black)
    screen.blit ( (x,y))
    x += d_x
    y += d_y
    if x + width >= 600 or x < 0:
        d_x = -d_x
    if y + height >= 400 or y < 0:
        d_y = -d_y
    screen.blit( (350,350))
    pygame.display.update()

    done = 0
    while not done:
        draw_stars(screen,stars,black)
        move_stars(stars)
        draw_stars(screen, stars, white)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE):
              done = 1
              break
            elif e.type == pygame.MOUSEBUTTONDOWN == 1:
              WINCENTER[:] = list(e.pos)
            clock.tick(50)

if __name__ == "__main__":
   main()