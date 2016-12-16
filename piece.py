import pygame

from random import randint
import numpy

import cell
import grid
from constants import *
import Piece_Structure

class Piece(cell.Cell):
	def __init__(self, grid, piece_type = BOX, upper_left=(col_grid / 2 ,0)):
		self.upper_left = upper_left
		if(piece_type == RANDOM):
			self.type = randint(1,7) 
		else: 
			self.type = piece_type
		self.grid = grid 
		self.cells_list = []
		self.coordList = []

		self.neighbor_down = []
		self.neighbor_right = []
		self.neighbor_left = [] 

		self._fixed = FALSE
		self.arrange_cells()
	
	arrange_cells=Piece_Structure.arrange_cells


	def set_fixed(self, fixed):
		self._fixed = fixed
		for element in self.coordList:
			cell = self.grid.get_cell(element)
			cell.set_fixed(fixed)

		if fixed:
			self.grid.update_score_fall()
			self.grid.update_level_fall()
			fixedSound=pygame.mixer.Sound("./sounds/newpiece.wav")
			fixedSound.play()

	def set_type(self, piece_type):
		self.type = piece_type
		for i in self.coordList:
			self.grid.get_cell(i).set_type(piece_type)

	def set_loc(self):
		self.upper_left = self.coordList[0]

	def set_neighbor_coords(self):
		self.RESET_surrounding()
		for ele in self.coordList:
			oneplus=ele[0]+1
			zeroplus=ele[0]
			oneminus= ele[0]-1

			oneplus1=ele[1]+1
			zeroplus1=ele[1]
			oneminus1= ele[1]-1
			right_coord = (oneplus, zeroplus1)
			down_coord = (zeroplus,oneplus1)
			left_coord = (oneminus ,zeroplus1)
			self.get_surrounding(rightDirection).append(self.grid.get_valid_coord(right_coord))
			self.get_surrounding(downDirection).append(self.grid.get_valid_coord(down_coord))
			self.get_surrounding(leftDirection).append(self.grid.get_valid_coord(left_coord))
		return TRUE

	def RESET_cells(self):
		self._fixed = FALSE
		for i in self.coordList:
			self.grid.get_cell(i).RESET()
		self.coordList = []

	def RESET_surrounding(self):
		self.neighbor_down = []
		self.neighbor_left = []
		self.neighbor_right = []

	def get_coords(self):
		return self.coordList

	def get_center(self):
		if (self.type == T or self.type == ShapeLTwo or self.type == ShapeLOne): return self.coordList[1]
		elif(self.type == ShapeSOne): return self.coordList[0]
		return (self.coordList[2])

	def get_type(self):
		return self.type

	def retrieve_x(self):
		temp=cells_list[0]
		return self.temp.retrieve_x()

	def get_y(self):
		temp=cells_list[0]
		return self.temp.get_y()

	def get_surrounding(self, direction):
		if(direction == downDirection):
			temp=self.neighbor_down
			return temp
		if(direction == leftDirection):
			temp=self.neighbor_left
			return temp
		if(direction == rightDirection): 
			temp=self.neighbor_right
			return temp

	def Clockwise_turn(self):
		Clockwise_turnd_coord = []
		if(self.type == BOX): return TRUE
		center = self.get_center()
		for i in self.coordList:
			centered_i = numpy.subtract(i, center)
			a= -centered_i[1]
			b=centered_i[0]
			temp_coord = (a, b)
			x=temp_coord[0]+center[0]
			y=temp_coord[1]+center[1]
			temp_coord[1]+center[1]
			Clockwise_turnd_coord.append((x, y))
		
		for i in Clockwise_turnd_coord:
			temp_coord = self.grid.get_valid_coord(i)
			f= FALSE
			t= TRUE
			if(temp_coord == SegError): return f
			if(self.grid.get_cell(temp_coord).is_fixed()): return t

		self.arrange_cells(Clockwise_turnd_coord)
		return t


	def is_fixed(self):
		return self._fixed

	def is_valid_surrounding(self, coords):
		for i in coords:
			if i == SegError: 
				return FALSE
		for i in coords:
			if(self.grid.get_cell(i).is_fixed()): 
				return FALSE
		return TRUE

	


	def leftMove(self, spaces=1):
		move_coordList = []

		if(self.is_valid_surrounding(self.get_surrounding(leftDirection))==FALSE):
			return INVALID

		move_coordList = self.get_surrounding(leftDirection)
		self.arrange_cells(move_coordList)
		return VALID

	

	def falldown_fast(self, spaces=1):
		move_coordList = []

		if(self.is_valid_surrounding(self.get_surrounding(downDirection))==FALSE):
			self.set_fixed(TRUE)
			return finished1

		
		move_coordList = self.get_surrounding(downDirection)
		self.arrange_cells(move_coordList)
		return VALID


	def rightMove(self, spaces=1):
		move_coordList = []

		if(self.is_valid_surrounding(self.get_surrounding(rightDirection))==FALSE):
			return INVALID

		move_coordList = self.get_surrounding(rightDirection)
		self.arrange_cells(move_coordList)
		return VALID

	def dropdown(self):
		if(self.falldown_fast()==finished1): 
			return (self.grid.clear_rows())

