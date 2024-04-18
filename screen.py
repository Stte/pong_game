import os

class Screen:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = [[' ' for _ in range(width)] for _ in range(height)]

	def set_cell(self, x, y, value):
		if self.screen[y][x] != value:
			self.screen[y][x] = value

	def print_screen(self):
		os.system('clear')
		for y in range(self.height):
			for x in range(self.width):
				print(self.screen[y][x], end='')
			print()

	def clear_screen(self):
		for y in range(self.height):
			for x in range(self.width):
				self.screen[y][x] = ' '
