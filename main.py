import pygame as pg
from settings import *
import sys


layer_size = (700, 500)
layer_pos = (90, 50)
layer = pg.Surface(layer_size)
layer_color = 'white'
layer.fill(layer_color)

pencil_color_one = 'black'
pencil_color_two = layer_color
pencil_size = 4

pg.init()
pg.display.set_caption('THE BEST PAINT!')
keys = {'LeftMouseBottom': False, 'RightMouseBottom': False}
def DrawRect(mpos, size):
    data = []
    for x in range(size):
        for y in range(size):
            x_target = mpos[0]-size//2 + x
            y_target = mpos[1]-size//2 + y
            data.append([x_target, y_target])
    return data

while True:
    mouse_pos = (pg.mouse.get_pos()[0] - layer_pos[0], pg.mouse.get_pos()[1] - layer_pos[1])
    if layer.get_rect().collidepoint(mouse_pos):
        if keys['LeftMouseBottom']:
            for pixel in DrawRect(mouse_pos, pencil_size):
                layer.set_at(pixel, pencil_color_one)
        if keys['RightMouseBottom']:
            for pixel in DrawRect(mouse_pos, pencil_size):
                layer.set_at(pixel, pencil_color_two)

    if pallet_rect.collidepoint(pg.mouse.get_pos()):
        for color in pallet_colors:
            rect = color[0].get_rect(topleft=color[1])
            if rect.collidepoint(pg.mouse.get_pos()):
                offset = (pg.mouse.get_pos()[0] - rect.left, pg.mouse.get_pos()[1] - rect.top)
                color = color[0].get_at(offset)
                if keys['LeftMouseBottom']:
                    pencil_color_one = color
                elif keys['RightMouseBottom']:
                    pencil_color_two = color




    display.fill((210, 222, 225))

    display.blit(pallet, pallet_rect)
    for color in pallet_colors:
        display.blit(color[0], color[1])
    display.blit(layer, layer_pos)

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