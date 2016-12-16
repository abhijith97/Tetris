import pygame

import grid
from constants import *

class Board(GamePlay):
	def __init__(self, grid, LeftCornerLocation=[0,0]):

		self.grid = grid
		self.width = self.grid.get_cell_size()
		self.height = self.grid.get_cell_size()
		self.rect = self.image.get_rect()
        #Set location of cell
		self.coord = self.grid.get_image_coord(self.LeftCornerLocation[0], self.LeftCornerLocation[1])
		self.rect.x = self.coord[0]
		self.rect.y = self.coord[1]


