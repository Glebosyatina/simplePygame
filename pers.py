import pygame
from time import sleep

num_pers = 0
pers_initx = 465
pers_inity = 605
pers_width = 100
pers_heigth = 60
class Pers:
	#по умолчанию медведь
	def __init__(self,window):
		self.window = window
		global points

		self.image = pygame.transform.scale(pygame.image.load('images/bear.png').convert_alpha(), (pers_width,pers_heigth))
		self.rect  = self.image.get_rect(center=(pers_initx, pers_inity))

		self.speed = 24  #скорость
		self.cur_point = -1    #текущая позиция
		global num_pers
		self.num   = num_pers # номер перса
		num_pers   += 1		

	#другой перс
	def other_image(self, image_path):
		self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (pers_width, pers_heigth))
		self.rect = self.image.get_rect(center=(pers_initx + 100*(num_pers-1), pers_inity))
		self.speed = 5

	#num - номер активного перса	
	#отрисовка перса и изменения позиции если этот перс активный сейчас
	def update(self, num):
		#получили массив событий нажатая клавиша будет True	
		keys = pygame.key.get_pressed()
		#проверяем нажатые клавиши и двигаем перса
		if self.num == num:
			if keys[pygame.K_UP]:
				if self.cur_point < 36:
					self.cur_point += 1
				self.rect.x = points[self.cur_point][0] - pers_width/2
				self.rect.y = points[self.cur_point][1] - pers_heigth/2
				#self.rect.y -= self.speed
				print(self.num, "x:", self.rect.x, "y:", self.rect.y)
				sleep(0.2)
			if keys[pygame.K_DOWN]:
				if self.cur_point > 0:
					self.cur_point -= 1
				self.rect.x = points[self.cur_point][0] - pers_width/2
				self.rect.y = points[self.cur_point][1] - pers_heigth/2
				#self.rect.y += self.speed			
				print(self.num, "x:", self.rect.x, "y:", self.rect.y)
				sleep(0.2)
        #отрисовка перса
		self.window.blit(self.image, self.rect)	

#координаты перебить
points = [
[160, 668],[98, 540],[249, 500],[314, 376],[415, 340],[560, 361],[647, 272],[736, 200],[845, 176],[951, 212],[1055, 272],[1179, 201],[1279, 315],[1398, 214],[1500, 287],[1478, 476],[1581, 554],[1704, 465],[1812, 519],[1805, 748], [1679, 717],[1623, 852],[1541, 881],[1459, 955],[1324, 953],[1228, 878],[1209, 710],[1102, 656],[979, 657],[939, 818], [859, 872],[770, 925],[635, 944],[511, 885],[428, 811],[352, 772],[240, 764]
]
		
