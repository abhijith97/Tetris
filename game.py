import pygame
from constants import *
Shuru = FALSE
Khalaas = FALSE
import output_text
import grid
import piece
import cell
from Loop import *

# class Game():

	# def __init__(self):
		# grid.Board.__init__():


def mainGame(display_Screen,font,logo):
	global Khalaas
	global Shuru
	m = output_text.Output_text(display_Screen, font)

	m.Beginning_Message()
	while not Shuru:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_e:
					Shuru = TRUE
				elif event.key == pygame.K_q:
					Shuru = TRUE
					Khalaas = TRUE
					pygame.quit()
					quit()

	preview_grid = grid.Board(4, 4, int((SC_HEIGHT-BORDER_GRID_SIZE)/row_grid), BLACK, [START_GRID_X_SMALL, BORDER_GRID_SIZE/2])
	preview_piece = piece.Piece(preview_grid, upper_left=[1,0])
	MainGameGrid = grid.Board(col_grid, row_grid, int((SC_HEIGHT-BORDER_GRID_SIZE)/row_grid), BLACK, [START_GRID_X, BORDER_GRID_SIZE/2])
	game_piece = piece.Piece(MainGameGrid)

	Loop(display_Screen, logo, MainGameGrid, preview_grid, game_piece, preview_piece, font, m)


	SecondLoop(display_Screen, logo, MainGameGrid, preview_grid, game_piece, preview_piece, font, m)
	
	pygame.quit()

