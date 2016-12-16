from constants import *
def arrange_cells(self, coordList=DEFAULT):
		self.RESET_cells()
		
		if(coordList == DEFAULT):

			if(self.type == BOX):
				self.coordList.append((self.upper_left[0], self.upper_left[1]))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+1))
				self.coordList.append((self.upper_left[0]+1, self.upper_left[1]))
				self.coordList.append((self.upper_left[0]+1, self.upper_left[1]+1))
			if(self.type == STICK):
				self.coordList.append((self.upper_left[0], self.upper_left[1]))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+1))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+2))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+3))


			if(self.type == ShapeLOne):
				self.coordList.append((self.upper_left[0], self.upper_left[1]))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+1))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+2))
				self.coordList.append((self.upper_left[0]+1, self.upper_left[1]+2))

			if(self.type == ShapeSOne):
				self.coordList.append((self.upper_left[0], self.upper_left[1]))
				self.coordList.append((self.upper_left[0]+1, self.upper_left[1]))
				self.coordList.append((self.upper_left[0]-1, self.upper_left[1]+1))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+1))
				

			if(self.type == ShapeSTwo):
				self.coordList.append((self.upper_left[0], self.upper_left[1]))
				self.coordList.append((self.upper_left[0]+1, self.upper_left[1]))
				self.coordList.append((self.upper_left[0]+1, self.upper_left[1]+1))
				self.coordList.append((self.upper_left[0]+1, self.upper_left[1]+2))

			if(self.type == T):
				self.coordList.append((self.upper_left[0], self.upper_left[1]))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+1))
				self.coordList.append((self.upper_left[0]+1, self.upper_left[1]+1))
				self.coordList.append((self.upper_left[0]-1, self.upper_left[1]+1))
			
			if(self.type == ShapeLTwo):
				self.coordList.append((self.upper_left[0], self.upper_left[1]))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+1))
				self.coordList.append((self.upper_left[0], self.upper_left[1]+2))
				self.coordList.append((self.upper_left[0]-1, self.upper_left[1]+2))

		elif(coordList!= DEFAULT):
			self.coordList = coordList
			
		for element in self.coordList:
			self.grid.get_cell(element).set_type(self.type)
		
		self.set_loc()
		self.set_neighbor_coords()
