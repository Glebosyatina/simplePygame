import pygame
from pers import Pers

pygame.init()
# Setting game window dimensions
window_width = 1280 
window_height = 720
game_display = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()

# Loading the image
bg_image = pygame.image.load('images/back.jpg').convert()
bg_image = pygame.transform.scale(bg_image, (window_width, window_height))

# Main game loop
running = True

#Pers
active_pers = 0

pers1 = Pers(game_display)
pers2 = Pers(game_display)
pers2.other_image('images/croc.png')
pers3 = Pers(game_display)
pers3.other_image('images/corgi.png')
pers4 = Pers(game_display)
pers4.other_image('images/shrek.png')

persons = list()
persons.append(pers1)
persons.append(pers2)
persons.append(pers3)
persons.append(pers4)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            my_key = event.key
            my_mod = event.mod
            print("pressed:", {pygame.key.name(my_key)})
            print("mod:", {my_mod})
            if event.key == pygame.K_1:
                active_pers = 1
            if event.key == pygame.K_2:
                active_pers = 2
            if event.key == pygame.K_3:
                active_pers = 3
            if event.key == pygame.K_4:
                active_pers = 4
            if event.key == pygame.K_0:
                active_pers = 0
    # Drawing image at position (0,0)
    game_display.blit(bg_image, (0, 0))
    for i in range(len(persons)):
        persons[i].update(active_pers)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
