import pygame
from time import sleep


num_pers = 0
pers_initx = 950
pers_inity = 670
pers_width = 100
pers_heigth = 60
class Pers:
	#по умолчанию капибара
	def __init__(self,window):
		self.window = window
		global points

		self.image = pygame.transform.scale(pygame.image.load('images/kapibara.png').convert_alpha(), (pers_width,pers_heigth))
		self.rect  = self.image.get_rect(center=(pers_initx, pers_inity))

		self.speed = 24  #скорость
		self.cur_point = -1    #текущая позиция
		global num_pers
		self.num   = num_pers + 1 # номер перса
		num_pers   += 1		

	#другой перс
	def other_image(self, image_path):
		self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (pers_width, pers_heigth))
		self.rect = self.image.get_rect(center=(pers_initx + 80*(num_pers-1), pers_inity))
		self.speed = 5

	#num - номер активного перса	
	#отрисовка перса и изменения позиции если этот перс активный сейчас
	def update(self, num):
		#получили массив событий нажатая клавиша будет True	
		keys = pygame.key.get_pressed()
		#проверяем нажатые клавиши и двигаем перса
		if self.num == num:
			if keys[pygame.K_RIGHT] and self.rect.x < 1130:
				self.rect.x += self.speed
				print(self.num, "x:", self.rect.x, "y:", self.rect.y)
			if keys[pygame.K_LEFT] and self.rect.x > 0:
				self.rect.x -= self.speed	
				print(self.num, "x:", self.rect.x, "y:", self.rect.y)
			if keys[pygame.K_UP]:
				if self.cur_point < 39:
					self.cur_point += 1
				self.rect.x = points[self.cur_point][0] - pers_width/2
				self.rect.y = points[self.cur_point][1] - pers_heigth/2
				#self.rect.y -= self.speed
				print(self.num, "x:", self.rect.x, "y:", self.rect.y)
				sleep(0.1)
			if keys[pygame.K_DOWN]:
				if self.cur_point > 0:
					self.cur_point -= 1
				self.rect.x = points[self.cur_point][0] - pers_width/2
				self.rect.y = points[self.cur_point][1] - pers_heigth/2
				#self.rect.y += self.speed			
				print(self.num, "x:", self.rect.x, "y:", self.rect.y)
				sleep(0.1)
		#отрисовка перса
		self.window.blit(self.image, self.rect)	

points = [
[1183, 599],[1090, 547],[1057, 463],[1109, 398],[1081, 312],[994, 295],[944, 362],[912, 449],[874, 529],[843, 621],[776, 666],[710, 598],[739, 517],[757, 429],[790, 341],[847, 283],[923, 246],[984, 178],[806, 169],[735, 230], [669, 282],[586, 312],[539, 378],[468, 432],[400, 501],[473, 536],[574, 549],[624, 628],[544, 666],[451, 669], [357, 654],[288, 586],[316, 507],[217, 521],[132, 504],[103, 412],[126, 326],[150, 234],[254, 218],[333, 142]
]
		
