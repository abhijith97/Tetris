import pygame

import cell
import piece
import game
from constants import *


#GET FUNCTIONS

def get_image_coord(self, col_num, row_num):
	a=self.LeftCornerLocation[0]
	b=self.LeftCornerLocation[1]
	temp=[a+self.size * col_num, b+self.size*row_num]
	return temp


def get_valid_coord(self,coord):
	if((0<= coord[0]) and (coord[0] < self.columns)) and ((0<= coord[1]) and (coord[1] < self.rows)):
		return coord
	return SegError

def get_cell(self, coord):
	for ele in self.cells_list:
		if(ele.is_cell(coord)): 
			return ele

	return FALSE

def get_cell_size(self):
	return self.size
def get_score(self):
	return self.score

def get_level(self):
	return self.level


def get_image_coord(self, col_num, row_num):
	return [self.LeftCornerLocation[0]+self.size * col_num, self.LeftCornerLocation[1]+self.size*row_num]
def get_valid_coord(self,coord):
	if((0<= coord[0] < self.columns) and (0<= coord[1] < self.rows)):
		return coord
	return SegError
def get_cell(self, coord):
	for i in self.cells_list:
		if(i.is_cell(coord)): 
			return i
	return FALSE

def get_cell_size(self):
	return self.size
def get_score(self):
	return self.score

def get_level(self):
	return self.level




class Board():
	def __init__(self, columns, rows, size, color, LeftCornerLocation=[0,0]):
		
		self.score = 0
		self.level = 1
		


		self.is_paused = FALSE
		self.color = color
		self.LeftCornerLocation = LeftCornerLocation
		self.columns = columns
		self.rows = rows
		self.size = size
		self.cells_list = []
		self.cell_group = pygame.sprite.Group()
		self.large_text = pygame.font.SysFont("monospace" ,50)
		self.small_text = pygame.font.SysFont("monospace" ,25)

		
		for j in range(rows):
			for i in range(columns):
				new_cell = cell.Cell(self, [i, j])
				self.cells_list.append(new_cell)
				self.cell_group.add(new_cell)



	def clear_rows(self):
		for i in range(self.rows):
			if(self.is_row_full(i)):
				self.update_score_remove()
				self.dropdown(i)
				i = 0 
		return finished1
	





	def update_score_remove(self):
		self.score += 100
		self.update_level_fall()
		


	def update_score_fall(self):
		self.score += 10

	def update_level_fall(self):
		self.level = self.score /  100 +1



	def is_empty(self, x, y):
		for i in self.cells_list:
			if(i.get_x() == x and i.get_y()==y): 
				return FALSE
			else: 
				return TRUE

	def is_row_full(self, row):
		for i in range(self.columns):
			if(self.get_cell((i,row)).is_fixed()==FALSE): 
				return FALSE
		return TRUE

	def draw_cells(self, display_Screen):
		for b in self.cells_list:
			b.draw(display_Screen)

	
	def is_game_over(self, display_Screen,font,m):
		for i in range(self.columns):
			if(self.get_cell((i,0)).is_fixed()):
				self.is_paused = TRUE
		if self.is_paused:
			Sound=pygame.mixer.Sound("./sounds/gameover.wav")
			Sound.play()
			return TRUE
		else: 
			return FALSE

	def RESET_game(self):
		self.score = 0
		for i in self.cells_list:
			i.RESET()

	def pause(self, display_Screen, font, logo, m):
		self.is_paused = TRUE
		m.Pause_Message()
		pygame.display.update()
		while(self.is_paused):
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						self.is_paused = FALSE
					elif event.key == pygame.K_q:
						pygame.quit()
					elif event.key == pygame.K_r:
						self.score = 0
						game.mainGame(display_Screen,font,logo)
		return TRUE

	def dropdown(self, row):
		for j in reversed(range(row+1)):
			for i in range(self.columns):
				if(j>=1):
					cell1 = self.get_cell((i,j))
					cell2 = self.get_cell((i,j-1))
					cell1.set_fixed(cell2.get_fixed())
					cell1.set_type(cell2.get_type())
					cell2.RESET()

	def display_text(self, pytext, text, location, display_Screen):
			label = pytext.render(text, 1, WHITE)
			display_Screen.blit(label,location)



	get_image_coord=get_image_coord
	get_valid_coord=get_valid_coord
	get_cell=get_cell
	get_cell_size=get_cell_size
	get_score=get_score
	get_level=get_level

	get_level=get_level
	get_score=get_score
	get_image_coord=get_image_coord
	get_valid_coord=get_valid_coord
	get_cell=get_cell
	get_cell_size=get_cell_size


