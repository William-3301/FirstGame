import pygame
import sys
import random 

pygame.init()
pygame.font.get_init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
clock = pygame.time.Clock()

size = 50
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
player_position = [screen_width/2,screen_height-2*size]
enemy_position = [random.randint(0,screen_width-size),50]
enemies = [enemy_position]


gameover = False

def drop_enemy(enemies):
	
	delay = random.random()

	if 	len(enemies) < 10 and delay < 0.1 :
			enemy_x =  random.randint(0,screen_width-size)
			enemy_y = 0
			enemies.append([enemy_x,enemy_y])

def draw_enemy(enemies):
	for enemy_position in enemies:
		pygame.draw.rect(screen,blue,(enemy_position[0],enemy_position[1],size,size))	

def enemy_falling(enemies):
	
	for idx,enemy_position in enumerate(enemies):
	 	
		if enemy_position[1] > 0 and enemy_position[1] < screen_height:
			enemy_position[1] += 5
		
		else:	
			enemy_position[1] = 1		
			enemy_position[0] = random.randint(0,screen_width-size)
			

def detect_collision(enemies,player_position):
	
	for enemy_position in enemies:
		
		enemy_x = enemy_position[0]
		enemy_y = enemy_position[1]
		player_x = player_position[0]
		player_y = player_position[1]

		if (enemy_x >= player_x and enemy_x < (size + player_x)) or (player_x > enemy_x  and player_x < (size + enemy_x)):
			if (enemy_y >= player_y and enemy_y < (size + player_y)) or (player_y > enemy_y  and player_y < (size + enemy_y)):
				return True


while not gameover:
		
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()


		
		else:
			
			if event.type == pygame.KEYDOWN:
				
				x = player_position[0]
				y = player_position[1]
				
				if player_position[0] == 0:
					if event.key == pygame.K_RIGHT:
						x += 50

				elif player_position[0] == (screen_width-size):
					if event.key == pygame.K_LEFT:
						x -= 50
				else:
					if event.key == pygame.K_LEFT:
						x -= 50
					elif event.key == pygame.K_RIGHT:
						x += 50

				player_position = [x,y]


	screen.fill(black)
	if detect_collision(enemies,player_position):
		gameover = True

	pygame.draw.rect(screen,red,(player_position[0],player_position[1],size,size))
	

	drop_enemy(enemies)
	draw_enemy(enemies)
	enemy_falling(enemies)

	
	clock.tick(60)
	pygame.display.update()
