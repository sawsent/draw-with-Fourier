import pygame
import sys
from statemanager import stateManager
from drawer import Drawer
from canvas import Canvas
from settings import *

class App:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Draw with Fourier Series')
		self.clock = pygame.time.Clock()
		self.stateManager = stateManager('canvas')
		self.drawer = Drawer(self.stateManager)
		self.canvas = Canvas(self.stateManager, self.drawer)
		self.states = {'canvas': self.canvas, 'drawer': self.drawer}   
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill((30, 30, 30))
			self.states[self.stateManager.get_state()].run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	app = App()
	app.run()