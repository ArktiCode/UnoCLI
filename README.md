# UNO CLI - Terminal Card Game

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A fully-featured single-player UNO card game built for the terminal, featuring AI opponents with adjustable difficulty levels. This project marks my **first major coding endeavor** as I transition into software development from engineering and gaming media.


## 🚀 Features

- **1vAI Gameplay**: Play against 1-3 CPU opponents
- **Smart AI**: Easy/Medium/Hard difficulty modes
- **AI Thinking Phase**: Includes a faux AI thinking phase to add immersion to the game
- **Standard UNO Rules**: Supports all special cards (Skip, Reverse, Draw 2/4, Wild)
- **Visual Turn Order**: Clear CLI display of game flow
- **Cross-Platform**: Runs on Windows (`.exe`) and Linux/Mac

## 📦 Installation
```bash
# Clone the repo
git clone https://github.com/ArktiCode/UnoCLI
cd UnoCLI

# Install dependencies (just PyInstaller if building EXE)
pip install -r requirements.txt

# Run the game
python main.py
```

## 🛠️ Build Your Own Executable
```bash
python compile.py  # Check /dist folder after
```

## 🎮 How to Play
```bash
1. Choose AI opponents and difficulty
2. Play cards matching color/number or use Wild cards
3. Type 'draw' to take a card
4. First player to have zero cards in their hand wins!
```

## 🌟 About This Project

As my first complete coding project, this UNO game represents:

- Start of my journey to transition as a **Software Programmer**
- Demonstration of **self-taught development skills**
- Foundation for **future game development projects**
- Implementation of **core Python concepts**:
```
  - Functions (Game Logic and AI decision-making)
  - Data Structures (Lists, Dictionaries, etc.)
  - OOP (Classes for Players, Game State and basic AI)
  - Control Flow (Loops for game rounds and turn management)
  - Error Handling (Input validation and game exceptions)
```
- Exposure to **Software Development Principles**:
```
  - OOP Design (Separation of game components)
  - CLI Interface (Interactive text-based gameplay)
  - Modular Architecture (Separate files for game logic, AI, and main program)
```
## 📜 License
```
MIT License - Free to use/modify with attribution. See LICENSE.
```

## Quote for the Project
```
"Every expert was once a beginner."
```

This project begins my journey into software development.
Feedback and contributions are always welcome!
