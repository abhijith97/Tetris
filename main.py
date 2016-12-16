import pygame

import output_text
import grid
import piece
import cell
import game
from constants import *


def main():


	pygame.init()

	font = pygame.font.SysFont(None,50)

	Khalaas = FALSE
	display_Screen = pygame.display.set_mode([SC_WIDTH, SC_HEIGHT])
	logo = pygame.image.load(image_folder+LOGO_IMAGE).convert()
	pygame.display.set_caption('Tetris')
	# gameobj=game.Game()
	game.mainGame(display_Screen,font,logo)

	print "Exiting... Thanks for playing the game !"


main()  
