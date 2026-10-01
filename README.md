# Spaceship Battle Game

A two-player spaceship battle game built with Python and Pygame.

Players control their spaceships, move around their side of the battlefield, fire bullets at each other, and try to reduce the opponent's health to zero.

## Features

- Two-player local multiplayer gameplay
- Yellow and Red spaceships
- Keyboard-based movement
- Bullet firing and collision detection
- Health system
- Winner screen
- Restart option after a match
- In-game controls screen
- FPS-controlled game loop
- Pygame-based graphics

## Controls

### Yellow Player

- `W` — Move Up
- `A` — Move Left
- `S` — Move Down
- `D` — Move Right
- `Left Ctrl` — Fire

### Red Player

- `↑` — Move Up
- `←` — Move Left
- `↓` — Move Down
- `→` — Move Right
- `Right Ctrl` — Fire

## How to Play

1. Run the game.
2. The controls screen will appear.
3. Press `ENTER` to start.
4. Move your spaceship using your assigned controls.
5. Fire bullets at the opponent.
6. Each successful hit reduces the opponent's health.
7. The first player to reduce the opponent's health to zero wins.
8. Press `R` on the winner screen to start a new match.
9. Press `ESC` to quit.

## Requirements

- Python 3.8 or later
- Pygame

## Installation

Install the required dependency:

    pip install -r requirements.txt

## Run the Game

Start the game with:

    python main.py

## Project Structure

    Spaceship-Battle-Game/
    ├── Assets/
    │   ├── Red_Spaceship.png
    │   ├── Yellow_Spaceship.png
    │   └── space.jpg
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    └── LICENSE

## Gameplay

Each player starts with 10 health points.

A maximum of 3 bullets can be active for each player at the same time.

The game ends when either player's health reaches zero.

## Author

**Hrishikesh Sharma**

GitHub: RaavanHrishi07

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.