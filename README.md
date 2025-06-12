# 8 Game Puzzle

## How to run

### Executable (Only Windows)
To run the game out of the box, go into the folder `executable` and double click in `Game.exe`

### Through Console

#### MacOS, python
To run this program in MacOS, python would need to be installed and a package called `pillow`.
- Install HomeBrew and folow instructions shown after installation

`brew install python`

- Install python

`brew install python`

- Verify python installation, (version could be different)

`python3.13 -V`

- Create virtual environment and activate it.

`python3.13 -m venv game`

`chmod a+x game/bin/activate`

`source game/bin/activate`

- Install pillow

`pip install pillow`

- Run the program

`python main.py`

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