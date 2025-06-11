from photos import MyPhoto, MyLabel
from heapq import heappush, heappop
from copy import deepcopy
class Node:
    def __init__(
        self,
        grid: list[list[tuple[int, int]]],
        empty_co: tuple[int, int],
        prev_node: 'Node',
    ):
        self.grid = grid
        self.grid_tuple = self.get_tuple_from_list()
        self.empty_co = empty_co
        self.heu_score = self.calculate_score()

        self.prev_node = prev_node

    def get_tuple_from_list(self):
        """Get a tuple from grid list"""
        return (tuple(self.grid[0]), tuple(self.grid[1]), tuple(self.grid[2]))

    def calculate_score(self):
        """Calculate the heuristic score of the grid."""
        score = 0
        for row in range(3):
            for col in range(3):
                goal = (row, col)
                curr = self.grid[row][col]
                score += abs(goal[0]-curr[0]) + abs(goal[1]-curr[1])
        return score
    
    def __lt__(self, value: 'Node'):
        return self.heu_score < value.heu_score
    
    def __gt__(self, value: 'Node'):
        return self.heu_score < value.heu_score


    def __eq__(self, value: 'Node'):
        return self.grid == value.grid and self.empty_co == value.empty_co
    
    def __hash__(self):
        return hash((self.grid_tuple, self.empty_co))

class Computer:
    def __init__(self, imagesList: list[MyPhoto], labelList: list[MyLabel]):
        self.Pqueue:list[tuple[int, Node]] = []
        self.imagesList = imagesList
        self.labelList = labelList
        (start_grid, empty) = self.grid_from_imagesList(imagesList)
        self.start_node = Node(start_grid, empty, None)
        heappush(self.Pqueue, (self.start_node.heu_score, self.start_node))

        # Do not know if it is possible to encounter a puzzle that is not
        # solvable
        self.impossible = False
        self.last_node = None
        self.create_decision_tree()
        # The steps are a list of grids
        self.steps: list[Node] = self.get_correct_steps()

    def get_correct_steps(self) -> list[Node]:
        """Get the order of steps to find solution."""
        if self.last_node is None:
            print("No steps available")
            return []

        curr_node = self.last_node
        steps = []
        while curr_node:
            steps.append(curr_node)
            curr_node = curr_node.prev_node

        # Remove the start_node which is in the end
        steps.pop()
        return steps

    def grid_from_imagesList(self, imagesList: list[MyPhoto]) -> tuple[list, tuple]:
        """Create a grid with the list of images.
         Also return the coordinates of the empty space.
        """
        grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        empty = (None, None)
        for image in imagesList:
            curr_row = image.curr_row
            curr_col = image.curr_col
            expected_row = image.expected_row
            expected_col = image.expected_col
            grid[curr_row][curr_col] = (expected_row, expected_col)
            if image.is_empty:
                empty = (curr_row, curr_col)
        
        print("EMPTY -> ", empty)
        print("GRID -> ", grid)
        return grid, empty
    
    def create_decision_tree(self):
        """Create the decision tree."""
        solved_puzzle = False
        visited = set()
        count = 0
        while self.Pqueue:
            count += 1
            #if count == 100:
            #    print("STAHPP")
            #    break
            current = heappop(self.Pqueue)
            print(current[1].grid)

            curr_score: int = current[0]
            curr_node: Node = current[1]

            empty_row = curr_node.empty_co[0]
            empty_col = curr_node.empty_co[1]
            curr_grid = curr_node.grid
            aux_node = None

            if curr_node.heu_score == 0:
                solved_puzzle = True
                self.last_node = curr_node
                break
            # Possible movements
            # DOWN
            if empty_row + 1 <= 2:
                aux_grid = deepcopy(curr_grid)
                aux_grid[empty_row+1][empty_col] = curr_grid[empty_row][empty_col]
                aux_grid[empty_row][empty_col] = curr_grid[empty_row+1][empty_col]
                aux_node = Node(aux_grid, (empty_row+1, empty_col), curr_node)
                if aux_node not in visited:
                    print("ADDED DOWN -> ", aux_node.grid)
                    heappush(self.Pqueue, (aux_node.heu_score, aux_node))
                else:
                    print("VISITED")

            # UP
            if empty_row - 1 >= 0:
                aux_grid = deepcopy(curr_grid)
                aux_grid[empty_row-1][empty_col] = curr_grid[empty_row][empty_col]
                aux_grid[empty_row][empty_col] = curr_grid[empty_row-1][empty_col]
                aux_node = Node(aux_grid, (empty_row-1, empty_col), curr_node)
                if aux_node not in visited:
                    print("ADDED UP -> ", aux_node.grid)
                    heappush(self.Pqueue, (aux_node.heu_score, aux_node))
                else:
                    print("VISITED")

            # RIGHT
            if empty_col + 1 <= 2:
                aux_grid = deepcopy(curr_grid)
                aux_grid[empty_row][empty_col+1] = curr_grid[empty_row][empty_col]
                aux_grid[empty_row][empty_col] = curr_grid[empty_row][empty_col+1]
                aux_node = Node(aux_grid, (empty_row, empty_col+1), curr_node)
                if aux_node not in visited:
                    print("ADDED RIGHT -> ", aux_node.grid)
                    heappush(self.Pqueue, (aux_node.heu_score, aux_node))
                else:
                    print("VISITED")

            # LEFT
            if empty_col - 1 >= 0:
                aux_grid = deepcopy(curr_grid)
                aux_grid[empty_row][empty_col-1] = curr_grid[empty_row][empty_col]
                aux_grid[empty_row][empty_col] = curr_grid[empty_row][empty_col-1]
                aux_node = Node(aux_grid, (empty_row, empty_col-1), curr_node)
                if aux_node not in visited:
                    print("ADDED LEFT -> ", aux_node.grid)
                    heappush(self.Pqueue, (aux_node.heu_score, aux_node))
                else:
                    print("VISITED")

            visited.add(curr_node)
            print("Finnish step")
        
        if not solved_puzzle:
            self.impossible = True


empty = (1, 1)
grid = [
    [(0, 0), (0, 2), (2, 1)],
    [(0, 1), (1, 2), (1, 0)],
    [(2, 2), (1, 1), (2, 0)]
]

next_grid = [
    [(0, 0), (0, 2), (2, 1)],
    [(0, 1), (1, 1), (1, 0)],
    [(2, 2), (1, 2), (2, 0)]
]