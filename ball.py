from map import Map
from collider import Collider

class Ball(Collider):
	def __init__(self, x, y, dx, dy, map: Map):
		self.x = x
		self.y = y
		self.width = 1
		self.height = 1
		self.dx = dx
		self.dy = dy
		self.map = map
		self.draw()

	def update_position(self):
		self.x += self.dx
		self.y += self.dy

		if self.y <= 0 or self.y >= self.map.height - 1:
			self.dy *= -1

	def reset_position(self):
		self.x = self.map.width // 2
		self.y = self.map.height // 2
		self.dx = -self.dx
		self.dy = -self.dy

	def draw(self):
		self.map.set_position(self.x, self.y, 'o')
