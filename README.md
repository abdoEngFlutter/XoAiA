# XO Search Arena — Human vs BFS AI

A Python console-based Tic-Tac-Toe game where a human (`X`) plays against an AI (`O`) that explores possible game states using **Breadth-First Search (BFS)**.

## Features

- Interactive 3×3 Tic-Tac-Toe board with numbered positions (1–9)
- BFS traversal of possible future game states using `collections.deque`
- Immediate winning moves and blocking moves prioritized
- Move selection based on the number of winning, drawing, and losing outcomes found by BFS
- Winner/draw detection and input validation
- Search statistics: explored states and execution time in milliseconds
- Replay option after each game

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Run locally

Clone this repository and navigate into it:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Run:

```bash
python main.py
```

On some systems, use `python3 main.py` instead.

## How to play

Choose a number corresponding to an empty square:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

You play as `X` and move first. The AI plays as `O`. Make three in a row to win.

## How the AI works

1. Generate each legal AI move and add its resulting board to a FIFO queue.
2. Explore subsequent human and AI moves **level by level** using BFS.
3. Record how many terminal paths end in an AI win, a draw, or a human win for each initial AI move.
4. Choose an immediate win if one exists; otherwise block an immediate human win.
5. Otherwise rank the moves by `(wins - losses) / total`, followed by draw rate, center/corner preference, and board position.

**Important:** This is a BFS-based heuristic AI, not minimax. It counts possible terminal paths rather than assuming an optimal opponent, so it is **not guaranteed to play perfectly**. Repeated board states reached by different move orders may be explored separately.

## Project structure

```text
XO-Search-Arena/
├── main.py       # Game logic, BFS search, and console interface
└── README.md     # Project documentation
```

## Technologies

- Python
- Breadth-First Search (BFS)
- `collections.deque` for the FIFO queue
- `time.perf_counter` for performance measurements

## GitHub upload

Create a new GitHub repository, then upload `main.py` and `README.md` using **Add file → Upload files → Commit changes**.

## License

For educational use. Add a LICENSE file if you want to specify redistribution permissions.
