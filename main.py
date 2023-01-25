import pygame as pg
from settings import *
import sys


layer_size = (500, 300)
layer = pg.Surface(layer_size)
layer_color = 'white'
layer.fill(layer_color)

pencil_color = 'black'
pencil_size = 4


pg.init()
pg.display.set_caption('THE BEST PAINT!')
keys = {'LeftMouseBottom': False, 'RightMouseBottom': False}
def rect(mpos, size):
    data = []
    for x in range(size):
        for y in range(size):
            x_target = mpos[0]-size//2 + x
            y_target = mpos[1]-size//2 + y
            data.append([x_target, y_target])
    return data

while True:
    mouse_pos = (pg.mouse.get_pos()[0] - 50, pg.mouse.get_pos()[1] - 50)
    if layer.get_rect().collidepoint(mouse_pos):
        #print(rect(mouse_pos, 4))
        if keys['LeftMouseBottom']:
            for pixel in rect(mouse_pos, pencil_size):
                layer.set_at(pixel, pencil_color)
        if keys['RightMouseBottom']:
            for pixel in rect(mouse_pos, pencil_size):
                layer.set_at(pixel, layer_color)
    display.fill((210, 222, 225))
    display.blit(layer, (50, 50))

    surf = pg.transform.scale(display, WIN_SIZE)
    screen.blit(surf, (0, 0))
    pg.display.flip()
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                keys['LeftMouseBottom'] = True
            if event.button == 3:
                keys['RightMouseBottom'] = True
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                keys['LeftMouseBottom'] = False
            if event.button == 3:
                keys['RightMouseBottom'] = False
        if event.type == pg.MOUSEWHEEL:
            if pencil_size >= 1:
                pencil_size += event.y
                print(pencil_size)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                pg.image.save(layer, 'Image.png')