import time, asyncio
from pynput import keyboard
from player import Player
from map import Map
from ball import Ball

class Pong:
	def __init__(self):
		self.listener = None
		self.FPS = 5
		self.game_running = False
		self.map = Map(25, 10)
		self.ball = Ball(self.map.width // 2, self.map.height // 2, 1, 1, self.map)
		self.player1 = Player(1, "Player 1", 1, self.map.height // 2, 3, self.map)
		self.player2 = Player(2, "Player 2", self.map.width - 2, self.map.height // 2, 3, self.map)
		print("Pong game initialized")
		self.start()

	def start(self):
		asyncio.run(self.game_loop())

	def stop(self):
		self.game_running = False

	def on_press(self, key):
		try:
			if key.char == 'w':
				self.player1.move_up = True
			elif key.char == 's':
				self.player1.move_down = True
			elif key.char == 'i':
				self.player2.move_up = True
			elif key.char == 'k':
				self.player2.move_down = True
		except AttributeError:
			pass

	def on_release(self, key):
		if key == keyboard.Key.esc:
			self.stop()
			return False

	def display_game(self):
		self.map.clear_screen()
		self.map.set_position(self.map.width // 2 - 2, 1, str(self.player1.score)) # Draw the scores
		self.map.set_position(self.map.width // 2 + 2, 1, str(self.player2.score)) # Draw the scores
		for i in range(self.map.height):
			self.map.set_position(self.map.width // 2, i, '.') # Draw the center line
		self.ball.draw()
		self.player1.draw()
		self.player2.draw()
		self.map.render()

	def update_game(self):
		self.ball.update_position()
		self.player1.update_position()
		self.player2.update_position()

		if self.ball.is_colliding(self.player1) or self.ball.is_colliding(self.player2):
			self.ball.dx *= -1

		if self.ball.x < 0:
			self.player2.score += 1
			self.ball.reset_position()
		elif self.ball.x >= self.map.width:
			self.player1.score += 1
			self.ball.reset_position()

	async def game_loop(self):
		self.game_running = True
		self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
		self.listener.start()
		try:
			while self.game_running:
				start_time = time.time()
				self.update_game()
				self.display_game()
				if self.player1.score >= 5 or self.player2.score >= 5:
					self.stop()
					print("Game Over")
				delta_time = time.time() - start_time
				sleep_time = 1./self.FPS - delta_time
				if (sleep_time > 0):
					await asyncio.sleep(sleep_time)
				print("-----------------")
		finally:
			self.listener.stop()


def main():
	Pong()

if __name__ == "__main__":
	main()
