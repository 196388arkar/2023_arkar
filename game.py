import pygame as pg

pg.init()

screen_width = 800
screen_height = 600

display = pg.display.set_mode((screen_width, screen_height))
display.fill('light blue', (0, 0, screen_width, screen_height))

#pg.display.set_caption('')
#icon_img = pg.image.load('resources/img/ufo.png')
#pg.display.set_icon(icon_img)

#background_img = pg.image.load('resources/img/background.png')
#display.blit(background_img, (0, 0))

sysfont = pg.font.SysFont('arial', 40)
text_img = sysfont.render('Аркар Мо Хтут', True, 'red')
#display.blit(text_img, (280, 500))
text1_img = sysfont.render('Hello', True, 'red')

#font = pg.fond.Fond('')
#game_over_img = font.render('Game Over', True, 'white')
w = text_img.get_width()
h = text_img.get_height()
x = screen_width/2 - w/2
y = screen_height - (h * 2)

running = True
while running:
    #display.fill('green', (200, 50, 10, 200))

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            running = False
        if event.type == pg.KEYUP and event.key == pg.K_a:
            print('Press a')
            display.blit(text_img, (x, y))
        if event.type == pg.KEYUP and event.key == pg.K_c:
            print('Press c')
            #display.blit('text1_img', (280, 500))
            display.fill('light blue', (0, 0, screen_width, screen_height))





pg.quit()