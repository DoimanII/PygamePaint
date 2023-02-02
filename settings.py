import pygame as pg

WIN_SIZE, WIN_RES = (800, 600), (800, 600)
screen = pg.display.set_mode(WIN_SIZE)
display = pg.Surface(WIN_SIZE)
clock = pg.time.Clock()



pallet = pg.image.load('assets/sprites/HUD/pallete_HUD.png').convert_alpha()
pallet_rect = pallet.get_rect(topleft=(10, 10))
pallet_colors = []

pallet_color = pg.Surface((32, 32))
pallet_color_pos = (13, 13)
pallet_color.fill('black')
pallet_colors.append((pallet_color, pallet_color_pos))

pallet_color = pg.Surface((32, 32))
pallet_color_pos = (13+5+32, 13)
pallet_color.fill('white')
pallet_colors.append((pallet_color, pallet_color_pos))
c = ['red', 'blue', 'green', 'grey', 'yellow']
ci = ['darkred', 'darkblue', 'darkgreen', 'darkgrey', 'orange']
for x in range(2):
    for y in range(5):
        yi = (13+32+5)+y*(32+5)
        xi = 13 + x*(32+5)
        pallet_color = pg.Surface((32, 32))
        if  x%2 == 0:
            pallet_color.fill(c[y])
        else:
            pallet_color.fill(ci[y])
        pallet_colors.append((pallet_color, (xi, yi)))