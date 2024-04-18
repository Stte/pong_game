from map import Map
from collider import Collider

class Player(Collider):
	def __init__(self, id, name, x, y, height, map: Map):
		self.id = id
		self.score = 0
		self.name = name
		self.x = x
		self.y = y
		self.height = height
		self.width = 1
		self.move_up = False
		self.move_down = False
		self.map = map
		self.draw()

	def go_up(self):
		if (self.y <= 0):
			return
		self.y -= 1

	def go_down(self):
		if (self.y + self.height >= self.map.height):
			return
		self.y += 1

	def update_position(self):
		if self.move_up:
			self.go_up()
			self.move_up = False
		elif self.move_down:
			self.go_down()
			self.move_down = False

	def draw(self):
		for y in range(self.y, self.y + self.height):
			for x in range(self.x, self.x + self.width):
				self.map.set_position(x, y, '|')

