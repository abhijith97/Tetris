
import pygame


import grid
from constants import *

# BLOCK CLASS
class Cell(pygame.sprite.Sprite):
	def __init__(self, grid, LeftCornerLocation=[0,0], cell_type = DEFAULT):
		
		pygame.sprite.Sprite.__init__(self)
		self.grid = grid
		self.LeftCornerLocation = LeftCornerLocation
		self.width = self.grid.get_cell_size()
		self.height = self.grid.get_cell_size()
		self.grade = 1
		self.border = 1
		self.type = cell_type
		self.fixed = FALSE
		self.image_list = []
		
		
		for i in IMAGE_NAMES:
			temp_image = pygame.image.load(image_folder+i).convert()
			temp_image = pygame.transform.scale(temp_image, (int(self.width), int(self.height)))
			self.image_list.append(temp_image)

		self.image = self.image_list[DEFAULT]
		self.rect = self.image.get_rect()
        
		self.coord = self.grid.get_image_coord(self.LeftCornerLocation[0], self.LeftCornerLocation[1])
		self.rect.x = self.coord[0]
		self.rect.y = self.coord[1]


	def set_type(self, cell_type):
		self.type = cell_type
	def set_x_loc(self,x):
		self.LeftCornerLocation[0] = x
	def set_y_loc(self,y):
		self.LeftCornerLocation[1] = y
	def set_visible(self, vis):
		self.is_visible = vis
	def set_fixed(self, fixed):
		self.fixed = fixed
		
	
	def RESET(self):
		self.set_type(DEFAULT)
		self.set_fixed(FALSE)
		self.is_visible = FALSE


	def retrieve_x(self):
		return self.LeftCornerLocation[0]
	def get_y(self):
		return self.LeftCornerLocation[1]
	def get_coord(self):
		return (self.LeftCornerLocation)
	def get_type(self):
		return self.type
	def get_fixed(self):
		return self.fixed


	
	def is_cell(self,LeftCornerLocation):
		if(self.LeftCornerLocation[0] == LeftCornerLocation[0]):
			if(self.LeftCornerLocation[1] == LeftCornerLocation[1]): 
				return TRUE
			else: 
				return FALSE

	def is_fixed(self):
		return self.fixed


	def imageLoader(self):
		self.image = self.image_list[self.get_type()]
		self.image = pygame.transform.scale(self.image, (int(self.width)-2, int(self.height)-2))
		self.rect = self.image.get_rect()

	def draw(self, display_Screen):
		self.imageLoader()
		self.coord = self.grid.get_image_coord(self.retrieve_x(), self.get_y())
		self.rect.x = self.coord[0]
		self.rect.y = self.coord[1]
		display_Screen.blit(self.image, (self.rect.x, self.rect.y))
