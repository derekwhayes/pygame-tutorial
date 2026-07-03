import pygame
from random import randint
from os.path import join

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')

# imports
player_surf = pygame.image.load(join('5games-main/space shooter/images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(2, -1)
player_speed = 300

meteor_surf = pygame.image.load(join('5games-main/space shooter/images', 'meteor.png')).convert_alpha()
meteor_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('5games-main/space shooter/images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

star_surf = pygame.image.load(join('5games-main/space shooter/images', 'star.png')).convert_alpha()

# random star coordinates
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    dt = clock.tick() / 1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgray')

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(meteor_surf, meteor_rect)

    # player movement
    player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surf, player_rect)

    if player_rect.left < 0:
        player_direction.x *= -1
        player_rect.left = 0
    if player_rect.right > WINDOW_WIDTH:
        player_direction.x *= -1
        player_rect.right = WINDOW_WIDTH
    if player_rect.top < 0:
        player_direction.y *= -1
        player_rect.top = 0;
    if player_rect.bottom > WINDOW_HEIGHT:
        player_direction.y *= -1
        player_rect.bottom = WINDOW_HEIGHT
    
    pygame.display.update()

pygame.quit()