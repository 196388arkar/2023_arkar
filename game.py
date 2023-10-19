import pygame as pg

pg.init()

screen_width = 800
screen_height = 600

display = pg.display.set_mode((screen_width, screen_height))
display.fill('light blue', (0, 0, screen_width, screen_height))

#pg.display.set_caption('')
#icon_img = pg.image.load('resources/img/ufo.png')
#pg.display.set_icon(icon_img)

background_img = pg.image.load('resources/img/background.png')
display.blit(background_img, (0, 0))

sysfont = pg.font.SysFont('arial', 40)
text_img = sysfont.render('Аркар Мо Хтут', True, 'red')
#display.blit(text_img, (280, 500))
#text1_img = sysfont.render('Hello', True, 'red')

#font = pg.fond.Fond('')
#game_over_img = font.render('Game Over', True, 'white')
w = text_img.get_width()
h = text_img.get_height()
x = screen_width/2 - w/2
y = screen_height - (h * 2)

#player
player_img = pg.image.load('resources/img/player.png')
player_width = player_img.get_width()
player_height = player_img.get_height()
player_x = screen_width/2 - player_width/2
player_y = screen_height - player_height
player_dx = 0
player_velocity = 2


bullet_img = pg.image.load('resources/img/bullet.png')
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()
bullet_x = player_x
bullet_y = player_y - bullet_height
bullet_dy = -10

bullet_visible = False


enemy_img = pg.image.load('resources/img/enemy.png')
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()
enemy_x = player_x
enemy_y = 0
enemy_dx = 0
enemy_dy = 1


import random


def enemy_create():
    global enemy_x, enemy_y
    enemy_x = random.randint(0, screen_width)
    enemy_x = 0


def bullet_create():
    global bullet_y, bullet_x, bullet_visible
    bullet_x = player_x
    bullet_y = player_y - bullet_height
    bullet_visible = True


def model_update():
    player_model()
    bullet_model()
    enemy_model()


def enemy_model():
    global enemy_x, enemy_y
    enemy_x += enemy_dx
    enemy_y += enemy_dy


def player_model():
    global player_x
    player_x = player_x + player_dx
    if player_x < 0:
        player_x = 0

    if player_x + player_width > screen_width:
        player_x = screen_width - player_width


def bullet_model():
    global bullet_visible, bullet_y
    if bullet_visible:
        bullet_y = bullet_y + bullet_dy
        if bullet_y < 0:
            bullet_visible = False
            print(f"{bullet_visible=}")

    rect_bullet = pg.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    rect_enemy = pg.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    if (rect_enemy.colliderect(rect_bullet)):
        print('BANG!')
        enemy_create()


def redraw():
    display.blit(background_img, (0, 0))
    display.blit(player_img, (player_x, player_y))
    if bullet_visible:
        display.blit(bullet_img, (bullet_x, bullet_y))

    pg.display.update()

def event_process():
    global player_dx
    running = True
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
            display.fill('light blue', (0, 0, screen_width, screen_height))
        if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            player_dx = - player_velocity
        if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            player_dx = player_velocity
        if event.type == pg.KEYUP and event.key == pg.K_LEFT:
            player_dx = 0
        if event.type == pg.KEYUP and event.key == pg.K_RIGHT:
            player_dx = 0

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            if not bullet_visible:
                bullet_create()
                print('Fire....')

    return running

running = True
while running:
    model_update()
    redraw()
    running = event_process()

pg.quit()