class Collider:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def is_colliding(self, other):
		# Check if the right edge of the first object is to the left of the left edge of the second object
		if self.x + self.width < other.x:
			return False
		# Check if the left edge of the first object is to the right of the right edge of the second object
		if self.x > other.x + other.width:
			return False
		# Check if the bottom edge of the first object is above the top edge of the second object
		if self.y + self.height -1 < other.y:
			return False
		# Check if the top edge of the first object is below the bottom edge of the second object
		if self.y > other.y + other.height -1:
			return False
		# If none of the above conditions are true, the objects are colliding
		return True
