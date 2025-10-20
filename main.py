import pygame
from pers import Pers

pygame.init()
# Setting game window dimensions
window_width = 1920 
window_height = 1080
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Неквиз')
clock = pygame.time.Clock()

# Loading the image
bg_image = pygame.image.load('images/karta.png').convert()
bg_image = pygame.transform.scale(bg_image, (window_width, window_height))

# Main game loop
running = True

#Pers
active_pers = 0

#создаем персов и привязываем нужные изображения
bear = Pers(game_display)

cat = Pers(game_display)
cat.other_image('images/cat.png')

cow = Pers(game_display)
cow.other_image('images/cow.png')

dog = Pers(game_display)
dog.other_image('images/dog.png')

fox = Pers(game_display)
fox.other_image('images/fox.png')

koala = Pers(game_display)
koala.other_image('images/koala.png')

lion = Pers(game_display)
lion.other_image('images/lion.png')

monkey = Pers(game_display)
monkey.other_image('images/monkey.png')

mouse = Pers(game_display)
mouse.other_image('images/mouse.png')

tiger = Pers(game_display)
tiger.other_image('images/tiger.png')

sova = Pers(game_display)
sova.other_image('images/sova.png')

zayats = Pers(game_display)
zayats.other_image('images/zayats.png')


persons = list()
persons.append(bear)
persons.append(cat)
persons.append(cow)
persons.append(dog)
persons.append(fox)
persons.append(koala)
persons.append(lion)
persons.append(monkey)
persons.append(mouse)
persons.append(tiger)
persons.append(sova)
persons.append(zayats)

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
			#выбор активного перса по нажатию цифры
            if event.key == pygame.K_1:
                if active_pers == 1:
                    active_pers = 11
                    break
                active_pers = 1
            if event.key == pygame.K_2:
                active_pers = 2
            if event.key == pygame.K_3:
                active_pers = 3
            if event.key == pygame.K_4:
                active_pers = 4
            if event.key == pygame.K_5:
                active_pers = 5
            if event.key == pygame.K_6:
                active_pers = 6
            if event.key == pygame.K_7:
                active_pers = 7
            if event.key == pygame.K_8:
                active_pers = 8
            if event.key == pygame.K_9:
                active_pers = 9
            if event.key == pygame.K_0:
				#10 перс и тд, то есть если сначала была нажата 1 потом 0
                if active_pers == 1:
                    active_pers = 10
                    break
                active_pers = 0

    # Drawing image at position (0,0)
    game_display.blit(bg_image, (0, 0))

    for i in range(len(persons)):
        persons[i].update(active_pers)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
