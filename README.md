# SPACE INVADERS
### A Python & Pygame Arcade Game

**A classic arcade-inspired space shooter built with Python and Pygame, featuring progressive difficulty, enemy projectiles, a mystery ship, scoring, lives and a multi-level game system.**

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Gameplay](#gameplay)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Object-Oriented Programming](#object-oriented-programming)
- [Installation and Setup](#installation-and-setup)
- [How to Run the Game](#how-to-run-the-game)
- [Building the Executable](#building-the-executable)
- [Testing and Quality Assurance](#testing-and-quality-assurance)
- [Code Quality](#code-quality)
- [Future Improvements](#future-improvements)
- [Credits and Acknowledgements](#credits-and-acknowledgements)
- [License](#license)

---

## Overview

Space Invaders is a desktop arcade game developed in Python using Pygame. The player controls a spaceship and must survive enemy attacks while progressing through increasingly challenging levels.

The project applies Object-Oriented Programming (OOP) principles to organise the game into separate classes, making the code easier to understand, maintain and extend.

The game was developed as a programming project with a focus on game development, software design, debugging, testing and the practical application of OOP.

## Features

- **Player-controlled spaceship:** Control the player's ship during gameplay.
- **Enemy formations:** Multiple alien enemies move and attack the player.
- **Projectile system:** Lasers are used for combat.
- **Mystery ship:** A special ship appears during gameplay.
- **Scoring system:** Earn points by defeating enemies.
- **Lives system:** Track the player's remaining lives.
- **Level progression:** Advance from Level 1 to Level 2.
- **Increasing challenge:** Later gameplay introduces changes to enemy formations and difficulty.
- **Collision detection:** Detect interactions between game entities and projectiles.
- **Game state management:** Handle gameplay, level progression, game-over conditions and victory.
- **Restart functionality:** Restart the game using the available restart controls.
- **Packaged desktop application:** The game can be distributed as a Windows executable with its required resources.

## Gameplay

The objective is to defeat the alien enemies, survive their attacks and complete both levels.

### Level 1
- Fight the initial alien formation.
- Avoid enemy projectiles.
- Protect the player's remaining lives.
- Earn points by defeating enemies.

### Level 2
- Progress to a more challenging stage.
- Face changes to the enemy formation and difficulty.
- Continue fighting until the level is completed.

The game displays a victory state after successfully completing Level 2. Losing all available lives triggers the relevant game-over behaviour.

### Controls

| Action | Control |
|---|---|
| Move the spaceship | Use the movement keys configured in the game |
| Fire lasers | Use the shooting key configured in the game |
| Restart | Use the implemented keyboard or mouse restart control |

*Note: Update this table with the exact keys and mouse actions implemented in the final version.*

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pygame | Graphics, input, sprites, sound and game loop |
| Object-Oriented Programming | Organising game entities and behaviour |
| PyInstaller | Packaging the game into a Windows executable |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
SPACE_INVADERS/
├── main.py
├── game.py
├── spaceship.py
├── alien.py
├── laser.py
├── obstacle.py
├── Font/
│   └── monogram.ttf
├── Graphics/
│   └── [Game image assets]
├── Sounds/
│   └── [Game sound assets]
├── README.md
└── requirements.txt
```

*The structure above is illustrative. Adjust it to match the actual files and folders in the submitted repository.*

### Main Components

- **`main.py`** — Initialises Pygame, creates the game window and runs the main application loop.
- **`game.py`** — Coordinates gameplay, manages game state, handles collisions, tracks scoring and lives, and controls level progression.
- **`spaceship.py`** — Implements the player's spaceship and its relevant behaviour.
- **`alien.py`** — Implements alien enemies and their relevant behaviour.
- **`laser.py`** — Implements projectile behaviour.
- **`obstacle.py`** — Implements obstacle objects where used.
- **`Font/`, `Graphics/` and `Sounds/`** — Store the game's visual, font and audio resources.

## Object-Oriented Programming

The project uses classes and objects to separate the responsibilities of different game entities and systems.

### Classes and Objects

Classes define the structure and behaviour of game entities. Objects are created from those classes during execution.

For example, multiple alien objects can be instantiated from the `Alien` class. This avoids creating a separate class for every individual enemy.

### Encapsulation

Related attributes and methods are grouped into classes. The `Spaceship` class handles player-related behaviour, while the `Alien` class handles enemy-related behaviour.

This organisation helps keep related functionality together.

### Inheritance

Where the game's entity classes inherit from `pygame.sprite.Sprite`, they reuse functionality provided by Pygame's sprite system.

This allows compatible game entities to be managed through sprite groups and used with Pygame's collision utilities.

### Cohesion

The classes are organised around related responsibilities. For example, player-specific behaviour belongs in `Spaceship`, while game-wide coordination belongs in `Game`.

Maintaining these responsibilities makes individual components easier to understand and modify.

### Coupling

The game systems interact to support gameplay. The `Game` class coordinates entities, groups and game states, while entity classes represent individual game objects.

A design goal is to minimise unnecessary dependencies between classes and use clear interfaces when they need to communicate.

*The descriptions above should be checked against the final source code. Only claim OOP features that are demonstrably implemented.*

## Installation and Setup

### Requirements

To run the source code, you need:

- Python 3
- Pygame
- The project's required fonts, graphics and sound files

### Install Dependencies

Open a terminal in the project directory and run:

```bash
python -m pip install pygame
```

If the project uses additional dependencies, install those listed in `requirements.txt`.

### Run from Python

From the project directory, run:

```bash
python main.py
```

Make sure the required asset folders remain in the locations expected by the source code.

## How to Run the Game

### Option 1: Run the Source Code

Run `main.py` using a Python installation with the required dependencies installed.

### Option 2: Run the Windows Executable

A packaged version can be distributed as a Windows application using PyInstaller.

1. Download and extract the complete packaged game.
2. Keep the executable and its supporting files together.
3. Launch `main.exe`.
4. Play without opening a code editor or IDE.

The packaged version must include all required resources, including fonts, graphics and sounds.

## Building the Executable

Install PyInstaller:

```bash
python -m pip install pyinstaller
```

From the project directory, package the application and its assets:

```bash
python -m PyInstaller --noconfirm --clean --onedir --windowed --add-data "Font;Font" --add-data "Graphics;Graphics" --add-data "Sounds;Sounds" main.py
```

This command is intended for Windows and assumes the listed asset folders exist at the project root and that the source code uses compatible resource paths.

The packaged application will be generated inside the `dist` directory.

**Important:** Test the executable after building it. If the game cannot locate an asset, correct the packaging configuration or resource paths before distributing the application.

## Testing and Quality Assurance

The game should be tested to confirm that its main features work as intended.

| Test area | Expected result |
|---|---|
| Application startup | The game window opens successfully. |
| Player movement | The spaceship responds to the configured controls. |
| Shooting | Projectiles behave as expected. |
| Enemy behaviour | Aliens move and attack as implemented. |
| Collision detection | Relevant projectile and entity collisions are handled. |
| Scoring | Score changes correctly when enemies are defeated. |
| Lives | The lives counter updates correctly. |
| Level progression | Completing Level 1 advances to Level 2. |
| Victory state | Completing Level 2 displays the win state. |
| Game-over state | Losing all lives triggers the game-over state. |
| Restart | The restart controls restore the appropriate game state. |
| Executable | The packaged application runs without requiring the IDE. |
| Assets | Fonts, graphics and sounds load correctly. |

Record the actual results of your tests before submission rather than marking untested features as successful.

## Code Quality

The project aims to follow these software development practices:

- **Readability:** Use descriptive variable and function names.
- **Maintainability:** Separate game entities and gameplay coordination into appropriate classes.
- **Efficiency:** Avoid unnecessary calculations and duplicated logic.
- **Robustness:** Test game states, collisions and restart behaviour.
- **Error handling:** Identify and resolve missing-resource and runtime errors.
- **Consistency:** Follow appropriate Python naming and formatting conventions, including PEP 8.
- **Documentation:** Use comments and docstrings to explain significant design decisions and OOP features.
- **Testing:** Verify gameplay features and the packaged application.

## Future Improvements

Possible extensions include:

- Additional levels with new enemy formations.
- More enemy types and attack patterns.
- Improved sound and visual effects.
- A settings menu for audio and controls.
- Persistent high scores.
- Additional automated tests.
- Improved error reporting for missing resources.

These are potential future improvements, not claims about features already implemented.

## Credits and Acknowledgements

This project was developed as a learning exercise in Python, Pygame, Object-Oriented Programming and desktop game development.

Credit original tutorials, asset creators, sound designers and other resources used in the project here. Make sure any third-party resources are acknowledged in accordance with their licence or usage requirements.

## License

No licence is specified by default. Add a licence only after deciding how the project and its included assets may be used and redistributed.
