# 8 Game Puzzle

## How to run

#### Executable
To run the game out of the box, go into the folder `executable` and double click in `Game.exe`

#### Through Console
To run the game from a console there is a setup needed:
- Install python (this game was tested with `python 3.12.2`)
- In this folder create a virtual environment and activate it (you can skip this step).
- Install dependency with pip: `pip install pillow`
- Run python program: `python main.py`

## In-game options

### Main menu

- Start game

Start the game by dividing the presented image into a grid of 3x3

- Select Image

Other images can be selected from the host computer. Click on `Select Image` to open the selector window and follow the procedure.

- Quit

Close the window

### Game stage

- Auto Solve

The pieces can be ordered automatically by the computer. Click `Auto Solve` to see the solution step by step.

- Main Menu

Return to the previous window `Main Menu`.

- Quit

Close the window.


## Code

### Algorithm

This project uses A start algorithm to create a decision tree from a grid, e.g.:

```
grid = [
    [(1, 1), (0, 1), (1, 2)],
    [(1, 0), (0, 2), (0, 0)],
    [(2, 0), (2, 1), (2, 2)]
]
```

Every `Node` knows its parent as `Node.prev_node` so after the decision tree finds a solution, the steps are appended to a list `Computer.steps`.

### Heuristic

To calculate the heuristic score this program uses the Manhattan distance. For example in the next grid:
```
grid = [
    [(1, 1), (0, 1), (1, 2)],
    [(1, 0), (0, 2), (0, 0)],
    [(2, 0), (2, 1), (2, 2)]
]

# From the position row=1, col=1
grid[1][1] -> (0, 2)

(1, 1) is the correct position but it has (0, 2)

heuristic_score = |(1 - 0) + (1 - 2)| = 2
```