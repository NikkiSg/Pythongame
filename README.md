# 🟡 Pacman AI Game (Python)

This project is a simplified version of the classic **Pacman game**, built using **Python** and **Pygame**. It features a player-controlled Pacman and an AI-controlled ghost (enemy) that adapts its behavior based on the player's position.

---

## 🚀 Features

- Basic movement for the player using arrow keys
- Enemy AI using a **rule-based technique**:
  - Ghost chases the player when nearby
  - Ghost wanders randomly when far away
- Modular file structure
- Integrated with **GitHub Actions** for test automation

---

## 📁 Project Structure

Pacman/
├── game.py # Main game loop
├── player.py # Player logic
├── enemy.py # Enemy AI logic
├── tests/ # Unit tests
│ ├── init.py
│ └── test_player.py
└── .github/
└── workflows/
└── python-app.yml # GitHub Actions CI

---

## 🧠 AI Technique Used

This project uses a **rule-based AI system** for the ghost:
- If the player is within 100 pixels, the ghost chases the player
- Otherwise, the ghost moves randomly

This approach adds dynamic behavior without complex pathfinding.

---

## 🛠️ Requirements

- Python 3.9+
- Pygame

Install dependencies:

```bash
pip install pygame

## ▶️ How to Run

1. CLone the repository
2. Run the game
```bash
python game.py

##🔬 Run Unit Test

```bash
python -m unittest discover -s Pacman/tests -p 'test_*.py'
