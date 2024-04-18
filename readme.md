# Pong Game

A simple Pong game implemented in Python, designed to be played in the terminal. This game has been tested and confirmed to work on VS Code terminal in a Linux environment.

## Features

- Two-player mode
- Scoring system
- Keyboard controls for player movement

## Requirements

- Python 3.x
- `pynput` library for keyboard input

## Installation

1. Clone the repository:
   git clone https://github.com/Stte/pong_game.git

2. Navigate to the project directory:
   `cd pong_game`

3. **Create a Python virtual environment** (optional but recommended):

   - On macOS/Linux:
     ```
     python3 -m venv venv
     ```

4. Activate the virtual environment:

   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required Python packages:
   `pip install -r requirements.txt`

## How to Play

- **Player 1**: Use 'W' to move up and 'S' to move down.
- **Player 2**: Use 'I' to move up and 'K' to move down.

The game ends when a player reaches a score of 5.

## Running the Game

To start the game, run the following command in the terminal:

`python3 pong.py`
