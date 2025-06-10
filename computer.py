from photos import MyPhoto, MyLabel
from heapq import heappush, heappop

grid = [
    [(2, 2), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (0, 0)],
]



class Node:
    def __init__(self, grid):
        self.grid = grid
        self.heu_score = self.calculate_score()

    def calculate_score(self):
        """Calculate the heuristic score of the grid."""
        score = 0
        for row in range(3):
            for col in range(3):
                goal = (row, col)
                curr = self.grid[row][col]
                score += abs(goal[0]-curr[0]) + abs(goal[1]-curr[1])
        return score

class Computer:
    def __init__(self, imagesList: list[MyPhoto], labelList: list[MyLabel]):
        self.Pqueue = []
        self.imagesList = imagesList
        self.labelList = labelList
        self.start_grid = self.grid_from_imagesList(imagesList)
        self.start_node = Node(self.start_grid)
        heappush(self.Pqueue, (self.start_node.heu_score, self.start_node))
    
    def grid_from_imagesList(self, imagesList: list[MyPhoto]):
        """Create a grid with the list of images."""
        grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        for image in imagesList:
            curr_row = image.curr_row
            curr_col = image.curr_col
            expected_row = image.expected_row
            expected_col = image.expected_col

            grid[curr_row][curr_col] = (expected_row, expected_col)
        
        return grid
