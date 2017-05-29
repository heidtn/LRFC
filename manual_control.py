import pygame
import cannon
import time

size = 240, 240
pygame.init()

screen = pygame.display.set_mode(size)

cannon = cannon.Cannon()

pan_angle = 0.
tilt_angle = 0.
pan_spd = 0
tilt_spd = 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            state = 0
            if event.type == pygame.KEYDOWN: state = 1

            if event.key == pygame.K_UP:
                tilt_spd = state
            if event.key == pygame.K_DOWN:
                tilt_spd = -state
            if event.key == pygame.K_LEFT:
                pan_spd = -state
            if event.key == pygame.K_RIGHT:
                pan_spd = state
            if event.key == pygame.K_SPACE and state:
                cannon.fire()

            if event.key ==  pygame.K_ESCAPE:
                pygame.quit()
                done = True

    pan_angle += pan_spd
    tilt_angle += tilt_spd
    cannon.set_pan_tilt(pan_angle, tilt_angle)
    time.sleep(0.1)

