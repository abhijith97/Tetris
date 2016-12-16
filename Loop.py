import pygame
import output_text
import grid
import piece
import cell
from constants import *
from game import *


def Quit():
	pygame.quit()
	quit()

def Loop(display_Screen, logo, MainGameGrid, preview_grid, game_piece, preview_piece, font, m):
	global Khalaas
	global Shuru
	while not Khalaas:
		display_Screen.fill(ORANGE)
		display_Screen.blit(logo, LOGO_POS)

		MainGameGrid.display_text(MainGameGrid.small_text, "Score: {}".format(MainGameGrid.get_score()), (20,150), display_Screen)
		MainGameGrid.display_text(MainGameGrid.small_text, "Level: {}".format(MainGameGrid.get_level()), (1400,150), display_Screen)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Quit()

			if event.type == pygame.KEYDOWN:
				# if event.key == pygame.K_a:
				# 	game_piece.leftMove()
				# if event.key == pygame.K_d:
				# 	game_piece.rightMove()
				if event.key == pygame.K_q:
					Khalaas = TRUE
				if event.key == pygame.K_SPACE:
					game_piece.falldown_fast()
				if event.key == pygame.K_s:
					game_piece.Clockwise_turn()
				if event.key == pygame.K_p:
					MainGameGrid.pause(display_Screen,font,logo,m)

		keys = pygame.key.get_pressed()
		if(keys[pygame.K_a]):
			game_piece.leftMove()
		if(keys[pygame.K_d]):
			game_piece.rightMove()
		if(keys[pygame.K_SPACE]):
			game_piece.falldown_fast()

					
		drop_loop = game_piece.dropdown()

		if(drop_loop == finished1):
			if(MainGameGrid.is_game_over(display_Screen,font,m)): 
				Khalaas = TRUE
			
			game_piece = piece.Piece(MainGameGrid, preview_piece.get_type())
			preview_piece.RESET_cells()
			preview_piece = piece.Piece(preview_grid, upper_left=[1,0])

		preview_grid.draw_cells(display_Screen)
		MainGameGrid.draw_cells(display_Screen)
		clock.tick(8 + MainGameGrid.get_score()/100)

		pygame.display.update()



def SecondLoop(display_Screen, logo, MainGameGrid, preview_grid, game_piece, preview_piece, font, m):
	global Khalaas
	global Shuru
	
	while Khalaas != FALSE:
		score = MainGameGrid.get_score()
		level = MainGameGrid.get_level()
		m.End_Message(score, level)
		# MainGameGrid.RESET_game()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
				if event.key == pygame.K_r:
					Khalaas = FALSE
					Shuru = FALSE
					mainGame(display_Screen, font, logo)
