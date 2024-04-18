from screen import Screen

class Map:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.map = Screen(width, height)

	def get_map(self):
		return self.map

	def set_position(self, x, y, value):
		if 0 <= x < self.width and 0 <= y < self.height:
			self.map.set_cell(x, y, value)
		else:
			print("Position out of bounds")

	def get_position(self, x, y):
		if 0 <= x < self.width and 0 <= y < self.height:
			return self.map[y][x]
		else:
			print("Position out of bounds")
			return None

	def render(self):
		self.map.print_screen()

	def clear_screen(self):
		self.map.clear_screen()
