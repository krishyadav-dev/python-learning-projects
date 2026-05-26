# Python Learning Projects

A collection of Python projects built while learning programming fundamentals. This repository documents my learning journey through hands-on coding, transitioning from simple terminal games to advanced Graphical User Interfaces (GUIs) and multi-module Object-Oriented Programming (OOP) designs.

---

## 📁 Repository Naming Conventions

To keep the repository clean and structured, directories and files follow a specific architectural convention highlighting the programming paradigm, interface style, and entry point layout:

### 1. Folder Suffixes (Paradigm & Interface)
Each project directory includes a suffix indicating the interface type and architectural pattern:
*   `**-CLI**` (Command Line Interface): Text-only interactive terminal applications.
*   `**-GUI**` (Graphical User Interface): Visual programs utilizing graphical windows (e.g., Python's `turtle` library).
*   `**-OOP**` (Object-Oriented Programming): Programs strongly centered around custom classes, objects, and encapsulation.
*   `**-OOP-CLI**`: Text terminal-based programs built entirely with Object-Oriented principles.
*   `**-OOP-GUI**`: Complex desktop programs and games utilizing both Object-Oriented architectures and graphical elements.

### 2. File Naming & Entry Points
*   **Procedural / Single-Module Projects:** The primary entry point file is named descriptively in `snake_case` according to the game/tool (e.g., `hangman.py`, `secret_auction.py`, `turtle_race.py`, `etch-a-sketch.py`).
*   **Modular / OOP-Based Projects:** The central starting block is standardized as `main.py`, supported by modular component files named after their classes or systems (e.g., `snake.py`, `paddle.py`, `coffee_maker.py`, `quiz_brain.py`).
*   **Art & Assets:** Text graphics, banner logos, and structural datasets are stored in separate files like `art.py`, `game_data.py`, or `<project_name>_art.py`.

---

## 🎮 Projects Catalogue

The repository currently features **16 projects** categorized by their interface and development approach:

### 1. ⌨️ CLI Games & Tools
Terminal-based interactive scripts demonstrating control flow, loops, collection data types (lists/dictionaries), and local game states.

| Project Name | Folder Location | Description | Entry Point |
| :--- | :--- | :--- | :--- |
| **Blackjack Capstone** | `cli-games-and-tools/Capstone_project-BlackJack-CLI/` | A fully featured console Blackjack game complete with custom card scoring, automated dealer strategies, and bankroll tracking. | `main.py` |
| **Rock Paper Scissors** | `cli-games-and-tools/Rock-Paper-Scissors-CLI/` | The classic hand game played against a computer opponent with detailed ASCII visual art for each move. | `Rock,Paper,Scissors!.py` |
| **Hangman** | `cli-games-and-tools/Hangman-CLI/` | Classic word-guessing game featuring dynamic ASCII hangman state rendering, letter-bank validation, and random vocabulary selection. | `hangman.py` |
| **Secret Auction** | `cli-games-and-tools/Secret-Auction-CLI/` | A blind auction simulator using terminal clearing commands to maintain bid privacy among multiple local participants. | `secret_auction.py` |
| **Accumulative Calculator** | `cli-games-and-tools/accumulative-calculator-CLI/` | Interactive CLI calculator allowing operations to be continuously chained over standard running totals. | `main.py` |
| **Higher-Lower Game** | `cli-games-and-tools/Higher-Lower-Game-CLI/` | A trivia-like console game comparing Instagram follower numbers of popular public personalities from mock game data. | `main.py` |
| **Number Guessing Game** | `cli-games-and-tools/Number-Guessing-Game-CLI/` | A guess-the-number game (1 to 100) featuring choice of Easy (10 attempts) and Hard (5 attempts) difficulties. | `main.py` |

### 2. 🎨 Graphical & Turtle Art GUI Programs
Interactive graphic programs utilizing the built-in standard Python `turtle` drawing engine.

| Project Name | Folder Location | Description | Key Mechanics / Entry Point |
| :--- | :--- | :--- | :--- |
| **Etch-A-Sketch** | `graphical-and-turtle-graphics/Etch-A-Sketch-App-GUI/` | An interactive drawing pad controlled via keyboard inputs (`W`/`S` to draw, `A`/`D` to steer, `C` to clear and reset). | `etch-a-sketch.py` |
| **Turtle Race Betting** | `graphical-and-turtle-graphics/Turtle-Race-Betting-Game-GUI/` | A colorful graphic turtle racing track. Players can place bets on which color turtle will cross the finish line first. | `turtle_race.py` |
| **Turtle Spirograph** | `graphical-and-turtle-graphics/Turtle-Spirograph-GUI/` | Generates a complex multi-layered spiral art layout using custom RGB color randomizers and math. | `main.py` |
| **Hirst spot Painting** | `graphical-and-turtle-graphics/hirst-painting/` | Generates a 10x10 dot matrix artwork inspired by Damien Hirst, using predefined color palettes and turtle movement steps. | `main.py` |

### 3. 🏗️ Object-Oriented Programming (OOP) Systems
Advanced projects highlighting the usage of custom Classes, constructor instantiations (`__init__`), data attributes, encapsulation, and visual canvas coordinate management.

| Project Name | Folder Location | Description | Main Architecture / Entry Point |
| :--- | :--- | :--- | :--- |
| **Coffee Machine** | `oop-and-modular-systems/Coffee_Machine-OOP/` | Simulation of a professional coffee machine. Built by splitting menus, payments, and resources into self-contained objects. | `main.py` |
| **Quiz Game** | `oop-and-modular-systems/quiz-game-OOP-CLI/` | An interactive trivia quiz engine separating game questions, data lists, and user progress metrics into structural objects. | `main.py` |
| **Snake Game** | `oop-and-modular-systems/Snake-Game-OOP-GUI/` | A desktop Snake retro-game implementing snake segment coordinate growth, collision detection, food spawning, and score saving. | `main.py` |
| **Pong Arcade Game** | `oop-and-modular-systems/Pong-Game-OOP-GUI/` | Real-time multi-player Pong arcade game complete with reflection vector angle shifts, paddle motion handlers, and scoreboard resets. | `main.py` |
| **Social Follower System** | `oop-and-modular-systems/Social-Follow-System-OOP-CLI/` | A modular proof-of-concept program modeling user follower and following relationship dynamics in software classes. | `main.py` |

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.7 or higher installed on your computer.
*   *Note: GUI programs require Python's Tkinter windowing interface (typically pre-installed with python).*

### Quick Play Guide

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/SlayerInferno/python-learning-projects.git
    cd python-learning-projects
    ```

2.  **Run any desired project directly:**
    Navigate to the project's subdirectory and launch the main script file. Here are some examples:

    *   **To play Blackjack (CLI):**
        ```bash
        cd cli-games-and-tools/Capstone_project-BlackJack-CLI
        python main.py
        ```

    *   **To play Snake Game (OOP-GUI):**
        ```bash
        cd oop-and-modular-systems/Snake-Game-OOP-GUI
        python main.py
        ```

    *   **To use the Etch-A-Sketch (GUI):**
        ```bash
        cd graphical-and-turtle-graphics/Etch-A-Sketch-App-GUI
        python etch-a-sketch.py
        ```

    *   **To play Rock Paper Scissors (CLI):**
        ```bash
        cd cli-games-and-tools/Rock-Paper-Scissors-CLI
        python "Rock,Paper,Scissors!.py"
        ```

---

## 📝 Project Structure

Below is an overview of the structural file tree layout across the repository:

```text
python-learning-projects/
├── README.md
├── LICENSE
├── .gitignore
│
├── cli-games-and-tools/
│   ├── Capstone_project-BlackJack-CLI/
│   │   ├── art.py
│   │   └── main.py
│   ├── Hangman-CLI/
│   │   ├── hangman.py
│   │   ├── hangman_art.py
│   │   └── hangman_words.py
│   ├── Higher-Lower-Game-CLI/
│   │   ├── art.py
│   │   ├── game_data.py
│   │   └── main.py
│   ├── Number-Guessing-Game-CLI/
│   │   ├── art.py
│   │   └── main.py
│   ├── Rock-Paper-Scissors-CLI/
│   │   └── Rock,Paper,Scissors!.py
│   ├── Secret-Auction-CLI/
│   │   ├── secret_auction.py
│   │   └── secret_auction_art.py
│   └── accumulative-calculator-CLI/
│       ├── art.py
│       └── main.py
│
├── graphical-and-turtle-graphics/
│   ├── Etch-A-Sketch-App-GUI/
│   │   └── etch-a-sketch.py
│   ├── Turtle-Race-Betting-Game-GUI/
│   │   └── turtle_race.py
│   ├── Turtle-Spirograph-GUI/
│   │   └── main.py
│   └── hirst-painting/
│       ├── HirstD-PyroninY_700_480x480.jpg
│       └── main.py
│
└── oop-and-modular-systems/
    ├── Coffee_Machine-OOP/
    │   ├── coffee_maker.py
    │   ├── menu.py
    │   ├── money_machine.py
    │   └── main.py
    ├── quiz-game-OOP-CLI/
    │   ├── data.py
    │   ├── question_model.py
    │   ├── quiz_brain.py
    │   └── main.py
    ├── Snake-Game-OOP-GUI/
    │   ├── food.py
    │   ├── scoreboard.py
    │   ├── snake.py
    │   └── main.py
    ├── Pong-Game-OOP-GUI/
    │   ├── paddle.py
    │   ├── pong_ball.py
    │   ├── scoreboard.py
    │   └── main.py
    └── Social-Follow-System-OOP-CLI/
        └── main.py
```

---

## 🎯 Learning Milestones Achieved

*   **Logic Controls:** Managing intricate application logic, state changes, nested loops, and deep conditions.
*   **Object-Oriented Architecture:** Designing structured classes, initializing states via arguments, encapsulation, and writing modular functions.
*   **Coordinate Math:** Driving vectors, movements, collision grids, boundaries, and angles using graphical models.
*   **File Modularity:** Dividing software responsibilities across different specialized component files (`import`, `from ... import`).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Coding!** 🚀