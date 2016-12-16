import pygame

from constants import *

class Output_text():
	def __init__(self, display_Screen, font):
		self.font = font
		self.display_Screen = display_Screen

	def Beginning_Message(self):
		self.display_Screen.fill(PEACH)

		outputFont = pygame.font.Font("./fonts/bar.ttf", 50)
		message = outputFont.render('TETRIS', TRUE, BLACK)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 120,100])
		
		outputFont = pygame.font.Font("./fonts/bar.ttf", 30)

		pygame.draw.rect(self.display_Screen, BLACK, [300 , 300, 50, 50])
		message = outputFont.render('A', TRUE, WHITE)
		self.display_Screen.blit(message, [310, 310])
		pygame.draw.rect(self.display_Screen, BLACK, [370 , 300, 50, 50])
		message = outputFont.render('D', TRUE, WHITE)
		self.display_Screen.blit(message, [380, 310])

		message = outputFont.render('to', TRUE, BLACK)
		self.display_Screen.blit(message, [460, 310])
		message = outputFont.render('MOVE', TRUE, RED)
		self.display_Screen.blit(message, [500, 310])

		pygame.draw.rect(self.display_Screen, BLACK, [750 , 300, 50, 50])
		message = outputFont.render('S', TRUE, WHITE)
		self.display_Screen.blit(message, [760, 310])

		message = outputFont.render('to', TRUE, BLACK)
		self.display_Screen.blit(message, [840, 310])
		message = outputFont.render('ROTATE', TRUE, RED)
		self.display_Screen.blit(message, [880, 310])

		pygame.draw.rect(self.display_Screen, BLACK, [320 , 380, 400, 50])
		message = outputFont.render('Space Bar', TRUE, WHITE)
		self.display_Screen.blit(message, [440, 387])
		message = outputFont.render('for', TRUE, BLACK)
		self.display_Screen.blit(message, [755, 390])
		message = outputFont.render('FASTER FALL', TRUE, RED)
		self.display_Screen.blit(message, [820, 390])
		
		
		
		message = outputFont.render('Press ', TRUE, BLACK)
		self.display_Screen.blit(message, [280,550])
		message = outputFont.render(' Q ', TRUE, RED)
		self.display_Screen.blit(message, [390,550])
		message = outputFont.render('to Quit', TRUE, BLACK)
		self.display_Screen.blit(message, [440,550])

		message = outputFont.render('Press ', TRUE, BLACK)
		self.display_Screen.blit(message, [280,500])
		message = outputFont.render(' E ', TRUE, RED)
		self.display_Screen.blit(message, [390,500])
		message = outputFont.render('to Start', TRUE, BLACK)
		self.display_Screen.blit(message, [440,500])

		message = outputFont.render('(Level up on earning 100 points)', TRUE, BLACK)
		self.display_Screen.blit(message, [590,600])

		pygame.display.update()


	def End_Message(self, score, level):
		self.display_Screen.fill(PEACH)
		outputFont = pygame.font.Font("./fonts/bar.ttf", 50)
		message = outputFont.render('GAME OVER', TRUE, RED)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 120,150])

		outputFont = pygame.font.Font("./fonts/bar.ttf", 30)
		message = outputFont.render('Score is ', TRUE, BLACK)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 250,250])
		message = outputFont.render(str(level), TRUE, RED)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 100,250])

		message = outputFont.render('Level is ', TRUE, BLACK)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 250,300])
		message = outputFont.render(str(score), TRUE, RED)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 100,300])

		message = outputFont.render('Press ', TRUE, BLACK)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 320,400])
		message = outputFont.render(' Q ', TRUE, RED)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 220,400])
		message = outputFont.render('to Quit', TRUE, BLACK)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 170,400])

		message = outputFont.render('Press ', TRUE, BLACK)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 320,450])
		message = outputFont.render(' R ', TRUE, RED)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 220,450])
		message = outputFont.render('to Restart', TRUE, BLACK)
		self.display_Screen.blit(message, [SC_WIDTH/2 - 170,450])

		pygame.display.update()

	def Pause_Message(self):
		w = SC_WIDTH/2
		h = 500
		pygame.draw.rect(self.display_Screen, PEACH, [(SC_WIDTH-w)/2 , (SC_HEIGHT-h)/2, w, h])
		message = self.font.render('GAME PAUSED', TRUE, RED)
		self.display_Screen.blit(message, [(SC_WIDTH-w)/2 + 120, (SC_HEIGHT-h)/2 + 10])
		message = self.font.render('C', TRUE, RED)
		self.display_Screen.blit(message, [(SC_WIDTH-w)/2 + 15, (SC_HEIGHT-h)/2 + 100])
		message = self.font.render(' to continue', TRUE, BLACK)
		self.display_Screen.blit(message, [(SC_WIDTH-w)/2 + 35, (SC_HEIGHT-h)/2 + 100])

		message = self.font.render('Q', TRUE, RED)
		self.display_Screen.blit(message, [(SC_WIDTH-w)/2 + 15, (SC_HEIGHT-h)/2 + 200])
		message = self.font.render(' to quit', TRUE, BLACK)
		self.display_Screen.blit(message, [(SC_WIDTH-w)/2 + 35, (SC_HEIGHT-h)/2 + 200])

		message = self.font.render('R', TRUE, RED)
		self.display_Screen.blit(message, [(SC_WIDTH-w)/2 + 15, (SC_HEIGHT-h)/2 + 300])
		message = self.font.render(' to restart', TRUE, BLACK)
		self.display_Screen.blit(message, [(SC_WIDTH-w)/2 + 35, (SC_HEIGHT-h)/2 + 300])
		pygame.display.update()

