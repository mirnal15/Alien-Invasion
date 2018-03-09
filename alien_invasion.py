
import pygame
from pygame.sprite import Group

from settings import Settings

from ship import Ship

from alien import Alien

import game_function as gf

def run_game():
	
	#initialize game and create a screen object.
	
	pygame.init()
	#now to create a display called screen on which the game will run.
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion-By MW")
	
	#make a ship
	ship = Ship(ai_settings,screen)
	
	#make an alien
	alien = Alien(ai_settings,screen)
	
	#make an empty group to store the bullets in.
	bullets = Group()
	
	#make an empty group to store the fleet of aliens in it.
	aliens = Group()
	#create the fleet of aliens
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#start the main loop for the program.
	while True:
		
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullet(bullets)
		#we update the alien's position after the bullets have been updated , because we'll soon be checking to see whether any bullets hit any alien.
		gf.update_aliens(aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		
run_game()
